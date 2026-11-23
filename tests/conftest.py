import http.server
import os
from pathlib import Path
import shutil
import socketserver
import subprocess
import sys
import threading
import tomllib

from playwright.sync_api import sync_playwright
import pytest


ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / "docs"
SITE_DIR = ROOT_DIR / "site"
LOCALES = ("pt", "en", "es")


def ensure_site_built():
    result = subprocess.run(
        [sys.executable, "-m", "zensical", "build"],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(
            f"zensical build failed (exit {result.returncode}):\n"
            f"{result.stdout}\n{result.stderr}"
        )


def find_chromium_executable():
    candidates = (
        os.environ.get("CHROMIUM_PATH"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("google-chrome"),
        "/snap/bin/chromium",
    )
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    return None


def chromium_launch_kwargs():
    headless = os.environ.get("HEADLESS", "1") != "0"
    kwargs = {
        "headless": headless,
        "args": ["--no-sandbox", "--disable-dev-shm-usage"],
    }
    chromium_path = find_chromium_executable()
    if chromium_path:
        kwargs["executable_path"] = chromium_path
    return kwargs


class QuietSiteHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIR), **kwargs)

    def log_message(self, format, *args):
        pass


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class LocalSiteServer:
    def __init__(self):
        self._server = None
        self._thread = None
        self.port = None

    def __enter__(self):
        self._server = ReusableTCPServer(("127.0.0.1", 0), QuietSiteHTTPHandler)
        self.port = self._server.server_address[1]
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._server is not None:
            self._server.shutdown()
            self._server.server_close()

    def url(self, path="/"):
        if not path.startswith("/"):
            path = "/" + path
        return f"http://127.0.0.1:{self.port}{path}"


@pytest.fixture(scope="session")
def built_site():
    ensure_site_built()
    return SITE_DIR


@pytest.fixture(scope="session")
def zensical_config(built_site):
    with (ROOT_DIR / "zensical.toml").open("rb") as f:
        return tomllib.load(f)


@pytest.fixture(scope="session")
def site_server(built_site):
    with LocalSiteServer() as server:
        yield server


@pytest.fixture(scope="session")
def browser(built_site):
    with sync_playwright() as playwright:
        instance = playwright.chromium.launch(**chromium_launch_kwargs())
        try:
            yield instance
        finally:
            instance.close()

