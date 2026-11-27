from html.parser import HTMLParser
import importlib.util
import json
import time
from urllib.parse import parse_qs, urlsplit

import pytest

from conftest import DOCS_DIR, LOCALES, ROOT_DIR


def load_build_playground_module():
    script_path = ROOT_DIR / "scripts" / "build_playground.py"
    spec = importlib.util.spec_from_file_location("build_playground", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EXAMPLES_BASE_URL = (
    "https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples"
)
EXPECTED_MEDIA_FILES = (
    "ginga.org.br/media_image.ncl",
    "ginga.org.br/media_video.ncl",
    "ginga.org.br/media_nclua.ncl",
    "ginga.org.br/media_ncl.ncl",
    "ginga.org.br/media_html.ncl",
)
EXPECTED_MEDIA_APP_URLS = tuple(f"{EXAMPLES_BASE_URL}/{f}" for f in EXPECTED_MEDIA_FILES)
EXPECTED_MEDIA_PLAYGROUND_URLS = tuple(
    f"https://ginga.org.br/gingaf/playground/?app={u}" for u in EXPECTED_MEDIA_APP_URLS
)
EXPECTED_HTML_FILES = (
    "image.html",
    "current_service.html",
)
EXPECTED_HTML_APP_URLS = tuple(f"{EXAMPLES_BASE_URL}/{f}" for f in EXPECTED_HTML_FILES)
EXPECTED_HTML_PLAYGROUND_URLS = tuple(
    f"https://ginga.org.br/gingaf/playground/?app={u}" for u in EXPECTED_HTML_APP_URLS
)
NON_ELEMENT_HANDBOOK_PAGES = {"about", "footer"}
ELEMENTS_WITHOUT_PLAYGROUND = {"ncl", "body"}


class HeaderPlaygroundParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_header = False
        self.playground_links = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == "header":
            self.in_header = True
        elif self.in_header and tag == "a":
            if "md-playground-button" in attr_map.get("class", "").split():
                self.playground_links.append(attr_map)

    def handle_endtag(self, tag):
        if tag == "header":
            self.in_header = False


class PlaygroundHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.div_stack = []
        self.playground_iframes = []
        self.playground_tabs = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        classes = set(attr_map.get("class", "").split())
        if tag == "div":
            self.div_stack.append("ginga-playground-container" in classes)
        elif tag == "iframe" and any(self.div_stack):
            self.playground_iframes.append(attr_map)
        elif tag == "button" and any(self.div_stack) and "ginga-playground-tab" in classes:
            self.playground_tabs.append(attr_map)

    def handle_endtag(self, tag):
        if tag == "div" and self.div_stack:
            self.div_stack.pop()


def assert_valid_playground_url(raw_url, expected_app_url=None):
    parsed = urlsplit(raw_url)
    assert parsed.scheme == "https"
    assert parsed.netloc == "ginga.org.br"
    assert parsed.path == "/gingaf/playground/"

    params = parse_qs(parsed.query)
    assert "app" in params
    assert len(params["app"]) == 1

    app_url = params["app"][0]
    parsed_app = urlsplit(app_url)
    assert parsed_app.scheme == "https"
    assert bool(parsed_app.netloc)
    assert app_url.startswith(f"{EXAMPLES_BASE_URL}/")
    if expected_app_url is not None:
        assert app_url == expected_app_url
    return app_url


@pytest.mark.parametrize("lang", LOCALES)
def test_header_playground_button_html_and_visibility(
    built_site, browser, site_server, lang
):
    html = (built_site / lang / "index.html").read_text(encoding="utf-8")
    parser = HeaderPlaygroundParser()
    parser.feed(html)
    assert len(parser.playground_links) == 1
    btn_attrs = parser.playground_links[0]
    assert btn_attrs.get("href") == "/gingaf/playground/"
    assert btn_attrs.get("target") == "_blank"
    rel_tokens = set(btn_attrs.get("rel", "").split())
    assert "noopener" in rel_tokens
    assert "noreferrer" in rel_tokens

    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        page.goto(site_server.url(f"/{lang}/"), wait_until="load", timeout=15000)
        btn = page.locator("header a.md-playground-button")
        assert btn.count() == 1
        assert btn.is_visible()
        assert btn.get_attribute("href") == "/gingaf/playground/"
    finally:
        context.close()


@pytest.mark.parametrize("lang", LOCALES)
def test_markdown_sources_embed_playground_iframe_and_switcher_tabs(lang):
    md_path = DOCS_DIR / lang / "gingancl" / "handbook" / "media.md"
    assert md_path.is_file(), f"Missing {md_path}"
    content = md_path.read_text(encoding="utf-8")

    parser = PlaygroundHTMLParser()
    parser.feed(content)

    assert len(parser.playground_iframes) == 1
    iframe = parser.playground_iframes[0]
    assert "ginga-playground" in iframe.get("class", "").split()
    assert_valid_playground_url(iframe.get("src", ""), EXPECTED_MEDIA_APP_URLS[0])

    assert len(parser.playground_tabs) == len(EXPECTED_MEDIA_APP_URLS)
    for idx, expected_app_url in enumerate(EXPECTED_MEDIA_APP_URLS):
        assert parser.playground_tabs[idx].get("aria-selected") == (
            "true" if idx == 0 else "false"
        )
        assert_valid_playground_url(
            parser.playground_tabs[idx].get("data-playground-src", ""),
            expected_app_url,
        )


@pytest.mark.parametrize("lang", LOCALES)
def test_built_html_renders_playground_iframe_and_tabs(built_site, lang):
    html_path = built_site / lang / "gingancl" / "handbook" / "media" / "index.html"
    assert html_path.is_file(), f"Missing {html_path}"
    html = html_path.read_text(encoding="utf-8")
    assert "&amp;lt;media&amp;gt;" not in html

    parser = PlaygroundHTMLParser()
    parser.feed(html)

    assert len(parser.playground_iframes) == 1
    iframe = parser.playground_iframes[0]
    assert "ginga-playground" in iframe.get("class", "").split()
    assert iframe.get("src") == EXPECTED_MEDIA_PLAYGROUND_URLS[0]
    assert_valid_playground_url(iframe.get("src", ""), EXPECTED_MEDIA_APP_URLS[0])
    assert iframe.get("title") is None
    assert iframe.get("loading") == "lazy"
    assert "fullscreen" in iframe.get("allow", "")

    assert len(parser.playground_tabs) == len(EXPECTED_MEDIA_PLAYGROUND_URLS)
    for idx, expected_pg_url in enumerate(EXPECTED_MEDIA_PLAYGROUND_URLS):
        assert parser.playground_tabs[idx].get("data-playground-src") == expected_pg_url


@pytest.mark.parametrize("lang", LOCALES)
def test_ncl_overview_page_embeds_playground_media_examples(built_site, lang):
    html_path = built_site / lang / "gingancl" / "index.html"
    assert html_path.is_file(), f"Missing {html_path}"
    parser = PlaygroundHTMLParser()
    parser.feed(html_path.read_text(encoding="utf-8"))

    assert len(parser.playground_iframes) == 1
    iframe = parser.playground_iframes[0]
    assert iframe.get("src") == EXPECTED_MEDIA_PLAYGROUND_URLS[0]
    assert iframe.get("title") is None
    assert iframe.get("loading") == "lazy"

    assert len(parser.playground_tabs) == len(EXPECTED_MEDIA_PLAYGROUND_URLS)
    for idx, expected_url in enumerate(EXPECTED_MEDIA_PLAYGROUND_URLS):
        assert parser.playground_tabs[idx].get("aria-selected") == (
            "true" if idx == 0 else "false"
        )
        assert parser.playground_tabs[idx].get("data-playground-src") == expected_url


@pytest.mark.parametrize("lang", LOCALES)
def test_html_apps_page_embeds_playground_html_examples(built_site, lang):
    html_path = built_site / lang / "gingahtml5" / "index.html"
    assert html_path.is_file(), f"Missing {html_path}"
    parser = PlaygroundHTMLParser()
    parser.feed(html_path.read_text(encoding="utf-8"))

    assert len(parser.playground_iframes) == 1
    iframe = parser.playground_iframes[0]
    assert iframe.get("src") == EXPECTED_HTML_PLAYGROUND_URLS[0]
    assert iframe.get("title") is None
    assert iframe.get("loading") == "lazy"

    assert len(parser.playground_tabs) == len(EXPECTED_HTML_PLAYGROUND_URLS)
    for idx, expected_url in enumerate(EXPECTED_HTML_PLAYGROUND_URLS):
        assert parser.playground_tabs[idx].get("aria-selected") == (
            "true" if idx == 0 else "false"
        )
        assert parser.playground_tabs[idx].get("data-playground-src") == expected_url


@pytest.mark.parametrize("lang", LOCALES)
def test_all_ncl_handbook_elements_embed_valid_playground_in_markdown_and_html(
    built_site, lang
):
    handbook_dir = DOCS_DIR / lang / "gingancl" / "handbook"
    element_files = [
        p
        for p in sorted(handbook_dir.glob("*.md"))
        if p.stem not in NON_ELEMENT_HANDBOOK_PAGES
    ]
    assert len(element_files) == 45

    for non_el in NON_ELEMENT_HANDBOOK_PAGES:
        non_el_md = handbook_dir / f"{non_el}.md"
        if non_el_md.is_file():
            non_el_parser = PlaygroundHTMLParser()
            non_el_parser.feed(non_el_md.read_text(encoding="utf-8"))
            assert non_el_parser.playground_iframes == []
            assert non_el_parser.playground_tabs == []

    for md_file in element_files:
        md_parser = PlaygroundHTMLParser()
        md_parser.feed(md_file.read_text(encoding="utf-8"))
        html_path = (
            built_site / lang / "gingancl" / "handbook" / md_file.stem / "index.html"
        )
        assert html_path.is_file(), f"Missing {html_path}"
        html_parser = PlaygroundHTMLParser()
        html_parser.feed(html_path.read_text(encoding="utf-8"))

        if md_file.stem in ELEMENTS_WITHOUT_PLAYGROUND:
            assert md_parser.playground_iframes == []
            assert md_parser.playground_tabs == []
            assert html_parser.playground_iframes == []
            assert html_parser.playground_tabs == []
            continue

        assert len(md_parser.playground_iframes) == 1, f"Missing iframe in {md_file}"
        assert len(md_parser.playground_tabs) >= 1, f"Missing tabs in {md_file}"
        assert len(html_parser.playground_iframes) == 1
        assert len(html_parser.playground_tabs) == len(md_parser.playground_tabs)

        iframe = html_parser.playground_iframes[0]
        assert "ginga-playground" in iframe.get("class", "").split()
        assert iframe.get("title") is None
        assert iframe.get("loading") == "lazy"
        assert "fullscreen" in iframe.get("allow", "")
        first_tab_src = html_parser.playground_tabs[0].get("data-playground-src", "")
        assert iframe.get("src") == first_tab_src
        assert_valid_playground_url(iframe.get("src", ""))

        for idx, tab in enumerate(html_parser.playground_tabs):
            expected_selected = "true" if idx == 0 else "false"
            assert tab.get("aria-selected") == expected_selected
            assert_valid_playground_url(tab.get("data-playground-src", ""))


def test_handbook_playgrounds_match_gingaf_catalog_tags():
    local_catalog = ROOT_DIR.parent / "gingaf" / "examples" / "catalog.json"
    if not local_catalog.is_file():
        pytest.skip("Sibling gingaf repository catalog.json not present locally")

    catalog_data = json.loads(local_catalog.read_text(encoding="utf-8"))
    raw_by_slug = {}
    for app_key, info in catalog_data.get("examples", {}).items():
        if not isinstance(info, dict):
            continue
        tags = info.get("ginga.org.br") or []
        assert len(tags) <= 3, f"{app_key} has {len(tags)} ginga.org.br tags (max 3)"
        if tags:
            assert info.get("category") != "multiuser", (
                f"Multiuser example {app_key} should not be tagged for basic NCL elements"
            )
        main_file = (info.get("mainFile") or "").strip()
        if not tags or not main_file:
            continue
        file_part, _, query_part = main_file.partition("?")
        clean_file = file_part.lstrip("/")
        if tags != ["html"]:
            assert clean_file.startswith("ginga.org.br/"), (
                f"{app_key} ({clean_file}) is outside examples/ginga.org.br/"
            )
        rank = (
            0
            if (
                info.get("category") == "ginga.org.br"
                or clean_file.startswith("ginga.org.br/")
            )
            else 1
        )
        app_url = f"{EXAMPLES_BASE_URL}/{clean_file}"
        pg_url = f"https://ginga.org.br/gingaf/playground/?app={app_url}" + (
            f"&{query_part}" if query_part else ""
        )
        for tag in tags:
            raw_by_slug.setdefault(str(tag).strip().lower(), []).append((rank, pg_url))

    expected_by_slug = {
        slug: [url for _, url in sorted(items, key=lambda pair: pair[0])]
        for slug, items in raw_by_slug.items()
    }
    expected_html_urls = expected_by_slug.pop("html", [])
    assert expected_html_urls == list(EXPECTED_HTML_PLAYGROUND_URLS)
    assert "ncl" not in expected_by_slug
    assert "body" not in expected_by_slug
    assert len(expected_by_slug) == 43
    for slug, urls in expected_by_slug.items():
        assert "/examples/ginga.org.br/" in urls[0], (
            f"Priority ginga.org.br/ example is not first for {slug}: {urls}"
        )

    for lang in LOCALES:
        ncl_md_path = DOCS_DIR / lang / "gingancl" / "index.md"
        assert ncl_md_path.is_file()
        ncl_md_parser = PlaygroundHTMLParser()
        ncl_md_parser.feed(ncl_md_path.read_text(encoding="utf-8"))
        assert [
            t.get("data-playground-src") for t in ncl_md_parser.playground_tabs
        ] == expected_by_slug["media"]

        html_md_path = DOCS_DIR / lang / "gingahtml5" / "index.md"
        assert html_md_path.is_file()
        html_md_parser = PlaygroundHTMLParser()
        html_md_parser.feed(html_md_path.read_text(encoding="utf-8"))
        assert [
            t.get("data-playground-src") for t in html_md_parser.playground_tabs
        ] == expected_html_urls

    for lang in LOCALES:
        for slug, expected_urls in expected_by_slug.items():
            md_path = DOCS_DIR / lang / "gingancl" / "handbook" / f"{slug}.md"
            assert md_path.is_file(), f"Missing {md_path}"
            parser = PlaygroundHTMLParser()
            parser.feed(md_path.read_text(encoding="utf-8"))
            actual_urls = [
                t.get("data-playground-src") for t in parser.playground_tabs
            ]
            assert actual_urls == expected_urls, f"Mismatch in {md_path}"


def test_build_playground_script_sync_and_idempotency(tmp_path):
    bp = load_build_playground_module()
    for lang, title_word in (("en", "Element"), ("pt", "Elemento"), ("es", "Elemento")):
        hb = tmp_path / lang / "gingancl" / "handbook"
        hb.mkdir(parents=True)
        (hb / "area.md").write_text(
            f'---\ntitle: "{title_word} &lt;area&gt;"\n---\n\n# &lt;area&gt;\n\nBody text.\n',
            encoding="utf-8",
        )
        (hb / "about.md").write_text(
            '---\ntitle: "About"\n---\n\n# About\n\nAbout text.\n',
            encoding="utf-8",
        )

    sample_catalog = {
        "examples": {
            "video": {
                "mainFile": "video.ncl",
                "category": "general",
                "ginga.org.br": ["area"],
            },
            "ncl_area": {
                "mainFile": "ginga.org.br/area.ncl",
                "category": "ginga.org.br",
                "ginga.org.br": ["area"],
            },
        }
    }

    first_count = bp.sync_handbook_playgrounds(sample_catalog, docs_dir=tmp_path)
    assert first_count == 3
    second_count = bp.sync_handbook_playgrounds(sample_catalog, docs_dir=tmp_path)
    assert second_count == 0

    for lang in LOCALES:
        area_md = (tmp_path / lang / "gingancl" / "handbook" / "area.md").read_text(
            encoding="utf-8"
        )
        parser = PlaygroundHTMLParser()
        parser.feed(area_md)
        assert len(parser.playground_iframes) == 1
        assert len(parser.playground_tabs) == 2
        assert parser.playground_tabs[0].get("data-playground-src", "").endswith(
            "/examples/ginga.org.br/area.ncl"
        )
        assert parser.playground_tabs[1].get("data-playground-src", "").endswith(
            "/examples/video.ncl"
        )
        assert "ginga-playground-container" not in (
            tmp_path / lang / "gingancl" / "handbook" / "about.md"
        ).read_text(encoding="utf-8")


def test_playground_styles_present_in_source_and_built_css(built_site):
    for css_path in (
        DOCS_DIR / "assets" / "stylesheets" / "extra.css",
        built_site / "assets" / "stylesheets" / "extra.css",
    ):
        assert css_path.is_file(), f"Missing {css_path}"
        css = css_path.read_text(encoding="utf-8")
        assert ".ginga-playground-container" in css
        assert ".ginga-playground-tabs" in css
        assert ".ginga-playground-tab" in css
        assert ".ginga-playground" in css
        assert "width: 100%" in css
        assert "height:" in css


@pytest.mark.parametrize("lang", LOCALES)
def test_browser_loads_playground_iframe_and_switches_between_image_and_video(
    browser, site_server, lang
):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    requested_playground_urls = []

    def handle_playground_route(route):
        requested_playground_urls.append(route.request.url)
        route.fulfill(
            status=200,
            content_type="text/html; charset=utf-8",
            body="<!DOCTYPE html><html><head><title>gingaf</title></head><body><div id='playground-stub'>ready</div></body></html>",
        )

    context.route("https://ginga.org.br/gingaf/playground/**", handle_playground_route)
    page = context.new_page()
    page_errors = []
    page.on("pageerror", lambda err: page_errors.append(str(err)))

    try:
        page.goto(
            site_server.url(f"/{lang}/gingancl/handbook/media/"),
            wait_until="load",
            timeout=15000,
        )

        iframe_el = page.locator("iframe.ginga-playground")
        assert iframe_el.count() == 1
        iframe_el.scroll_into_view_if_needed()

        box = iframe_el.bounding_box()
        assert box is not None
        assert box["width"] >= 300
        assert box["height"] >= 500
        assert EXPECTED_MEDIA_PLAYGROUND_URLS[0] in requested_playground_urls

        tabs = page.locator("button.ginga-playground-tab")
        assert tabs.count() == 5
        expected_labels = (
            "media_image.ncl",
            "media_video.ncl",
            "media_nclua.ncl",
            "media_ncl.ncl",
            "media_html.ncl",
        )
        for idx, label in enumerate(expected_labels):
            assert tabs.nth(idx).inner_text().strip() == label
            assert tabs.nth(idx).get_attribute("aria-selected") == (
                "true" if idx == 0 else "false"
            )

        tabs.nth(1).click()
        assert tabs.nth(0).get_attribute("aria-selected") == "false"
        assert tabs.nth(1).get_attribute("aria-selected") == "true"
        assert iframe_el.get_attribute("src") == EXPECTED_MEDIA_PLAYGROUND_URLS[1]

        page.wait_for_function(
            "expected => Array.from(document.querySelectorAll('iframe.ginga-playground')).some(f => f.src === expected)",
            arg=EXPECTED_MEDIA_PLAYGROUND_URLS[1],
            timeout=5000,
        )
        deadline = time.time() + 5
        while (
            EXPECTED_MEDIA_PLAYGROUND_URLS[1] not in requested_playground_urls
            and time.time() < deadline
        ):
            page.wait_for_timeout(50)
        assert EXPECTED_MEDIA_PLAYGROUND_URLS[1] in requested_playground_urls

        assert page_errors == []
    finally:
        context.close()

