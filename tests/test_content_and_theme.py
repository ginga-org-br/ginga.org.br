from html.parser import HTMLParser
import importlib.util
import posixpath
import re
from types import SimpleNamespace
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import pytest

from conftest import DOCS_DIR, LOCALES, ROOT_DIR, SITE_DIR


def load_deploy_folder_module():
    script_path = ROOT_DIR / "scripts" / "deploy_folder.py"
    spec = importlib.util.spec_from_file_location("deploy_folder", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def collect_nav_files(node):
    entries = []
    if isinstance(node, list):
        for item in node:
            entries.extend(collect_nav_files(item))
    elif isinstance(node, dict):
        for title, value in node.items():
            if isinstance(value, str):
                entries.append((title, value))
            else:
                entries.extend(collect_nav_files(value))
    return entries


def md_path_to_site_html(rel_md_path):
    posix_path = rel_md_path.replace("\\", "/")
    if posix_path.endswith("/index.md"):
        return SITE_DIR / posix_path[:-len("index.md")] / "index.html"
    if posix_path == "index.md":
        return SITE_DIR / "index.html"
    return SITE_DIR / posix_path[:-len(".md")] / "index.html"


class AssetAndLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.srcs = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == "a" and "href" in attr_map:
            self.hrefs.append(attr_map["href"])
        elif tag == "img" and "src" in attr_map:
            self.srcs.append(attr_map["src"])


def test_zensical_config_nav_matches_docs_on_disk(zensical_config):
    nav_entries = collect_nav_files(zensical_config["project"]["nav"])
    nav_paths = {path for _, path in nav_entries}
    disk_paths = {
        p.relative_to(DOCS_DIR).as_posix() for p in DOCS_DIR.rglob("*.md")
    }

    assert len(nav_entries) == len(nav_paths), (
        "Duplicate documentation entries detected in zensical.toml nav."
    )
    assert sorted(nav_paths - disk_paths) == []
    assert sorted(disk_paths - nav_paths) == []


def test_all_nav_pages_built_with_nonempty_html(built_site, zensical_config):
    nav_entries = collect_nav_files(zensical_config["project"]["nav"])
    for _, rel_md in nav_entries:
        html_path = md_path_to_site_html(rel_md)
        assert html_path.is_file(), f"Missing built HTML {html_path}"
        assert html_path.stat().st_size > 0


def test_configured_assets_sitemap_and_pdfs(built_site, zensical_config):
    project = zensical_config["project"]
    for rel_path in project.get("extra_javascript", []):
        assert (DOCS_DIR / rel_path).is_file()
        assert (built_site / rel_path).is_file()

    for rel_path in project.get("extra_css", []):
        assert (DOCS_DIR / rel_path).is_file()
        assert (built_site / rel_path).is_file()

    theme = project.get("theme", {})
    for key in ("logo", "favicon"):
        rel_path = theme.get(key)
        if rel_path:
            assert (DOCS_DIR / rel_path).is_file()
            assert (built_site / rel_path).is_file()

    snippets = (
        project.get("markdown_extensions", {})
        .get("pymdownx", {})
        .get("snippets", {})
    )
    for inc_path in snippets.get("auto_append", []):
        assert (ROOT_DIR / inc_path).is_file()

    sitemap_path = built_site / "sitemap.xml"
    assert sitemap_path.is_file()
    tree = ET.parse(sitemap_path)
    locs = [
        elem.text
        for elem in tree.getroot().iter()
        if elem.tag.endswith("loc") and elem.text
    ]
    assert len(locs) > 0
    for lang in LOCALES:
        assert any(f"/{lang}/" in loc for loc in locs)

    src_pdfs = sorted((DOCS_DIR / "assets" / "pdf").glob("*.pdf"))
    assert len(src_pdfs) > 0
    for src_pdf in src_pdfs:
        built_pdf = built_site / "assets" / "pdf" / src_pdf.name
        assert built_pdf.is_file(), f"Missing built PDF {built_pdf}"
        assert built_pdf.read_bytes().startswith(b"%PDF-")
        assert built_pdf.stat().st_size == src_pdf.stat().st_size


def test_no_broken_internal_links_or_images(built_site):
    broken_links = []
    broken_images = []

    for html_file in sorted(built_site.rglob("*.html")):
        rel_dir = html_file.relative_to(built_site).parent.as_posix()
        if rel_dir == ".":
            rel_dir = ""

        parser = AssetAndLinkParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="ignore"))

        for items, bucket in (
            (parser.hrefs, broken_links),
            (parser.srcs, broken_images),
        ):
            for raw in items:
                if not raw or raw.startswith(
                    ("#", "mailto:", "tel:", "javascript:", "data:")
                ):
                    continue
                parsed = urlsplit(raw)
                if parsed.scheme in ("http", "https"):
                    continue
                path = unquote(parsed.path)
                if not path or path == "/gingaf" or path.startswith("/gingaf/"):
                    continue
                if path.startswith("/"):
                    resolved = posixpath.normpath(path.lstrip("/"))
                else:
                    resolved = posixpath.normpath(posixpath.join(rel_dir, path))
                if resolved == ".":
                    resolved = ""
                target = built_site / resolved
                exists = target.is_file() or (
                    target.is_dir() and (target / "index.html").is_file()
                )
                if not exists:
                    bucket.append(
                        (html_file.relative_to(built_site).as_posix(), raw, resolved)
                    )

    assert broken_links == []
    assert broken_images == []


@pytest.mark.parametrize("lang", LOCALES)
def test_handbook_xml_tag_titles_are_escaped_in_navigation(built_site, lang):
    critical_tags = ("area", "body", "head", "link", "media", "meta")
    html = (built_site / lang / "index.html").read_text(encoding="utf-8")
    match = re.search(
        r'<nav class="md-nav md-nav--primary".*?</nav>\s*</div>',
        html,
        re.S,
    )
    assert match is not None
    nav_html = match.group(0)
    for tag_name in critical_tags:
        assert f"&lt;{tag_name}&gt;" in nav_html
        assert not re.search(
            rf'<span class="md-ellipsis">\s*<{tag_name}>\s*</span>', nav_html
        )


def test_handbook_element_pages_render_tables_and_frontmatter(built_site):
    for lang in LOCALES:
        handbook_dir = DOCS_DIR / lang / "gingancl" / "handbook"
        for md_file in sorted(handbook_dir.glob("*.md")):
            if md_file.stem in ("about", "footer"):
                continue
            md_text = md_file.read_text(encoding="utf-8")
            assert md_text.startswith("---\n")
            assert "title:" in md_text.split("---", 2)[1]

            built_html = (
                built_site
                / lang
                / "gingancl"
                / "handbook"
                / md_file.stem
                / "index.html"
            )
            assert built_html.is_file()
            html = built_html.read_text(encoding="utf-8")
            assert "<table" in html


def test_theme_palette_toggle_switches_color_scheme(browser, site_server):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        page.goto(site_server.url("/en/"), wait_until="load", timeout=15000)
        assert page.locator("body").get_attribute("data-md-color-scheme") == "default"

        page.locator("label[for='__palette_1']").click()
        page.wait_for_function(
            "() => document.body.getAttribute('data-md-color-scheme') === 'slate'",
            timeout=5000,
        )

        page.locator("label[for='__palette_0']").click()
        page.wait_for_function(
            "() => document.body.getAttribute('data-md-color-scheme') === 'default'",
            timeout=5000,
        )
    finally:
        context.close()


@pytest.mark.parametrize("lang", LOCALES)
def test_custom_assets_load_on_locales(browser, site_server, lang):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    responses = []
    page.on("response", lambda r: responses.append((r.status, r.url)))
    try:
        page.goto(site_server.url(f"/{lang}/"), wait_until="load", timeout=15000)
        assert any(
            status == 200 and url.endswith("/assets/stylesheets/extra.css")
            for status, url in responses
        )
        assert any(
            status == 200 and url.endswith("/assets/javascripts/extra.js")
            for status, url in responses
        )
    finally:
        context.close()


def test_key_pages_load_without_page_errors(browser, site_server):
    paths = (
        "/pt/",
        "/en/",
        "/es/",
        "/en/standards/",
        "/en/development-tools/",
        "/en/guides/tv3.0-architecture/",
        "/en/gingancl/",
        "/en/gingahtml5/",
        "/en/gingaccwebservices/",
        "/en/gingaj/",
    )
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        for path in paths:
            page_errors = []
            on_error = lambda err: page_errors.append(str(err))
            page.on("pageerror", on_error)
            response = page.goto(
                site_server.url(path),
                wait_until="domcontentloaded",
                timeout=15000,
            )
            page.remove_listener("pageerror", on_error)
            assert response is not None
            assert response.status == 200
            assert page.locator("h1").count() >= 1
            assert page_errors == []
    finally:
        context.close()


def test_deploy_folder_script_validates_mount_and_invokes_rsync(monkeypatch, tmp_path):
    df = load_deploy_folder_module()
    assert df.deploy_folder("") == 1

    monkeypatch.setattr(df, "find_mount_dir", lambda p: None)
    assert df.deploy_folder(str(tmp_path)) == 1

    recorded_cmds = []
    monkeypatch.setattr(df, "find_mount_dir", lambda p: "/mnt/ftpes")
    monkeypatch.setattr(df, "get_fstype", lambda m: "fuse.rclone")

    def fake_run(cmd, **kwargs):
        recorded_cmds.append(cmd)
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(df.subprocess, "run", fake_run)
    rc = df.deploy_folder("/mnt/ftpes/public_html", site_dir=tmp_path / "site")
    assert rc == 0
    assert len(recorded_cmds) == 1
    assert recorded_cmds[0][:3] == ["rsync", "-rlptcO", "--delete-after"]
    assert "/gingaf" in recorded_cmds[0]
    assert recorded_cmds[0][-1] == "/mnt/ftpes/public_html"
