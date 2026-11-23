from html.parser import HTMLParser
import time
from urllib.parse import parse_qs, urlsplit

import pytest

from conftest import DOCS_DIR, LOCALES


EXPECTED_IMAGE_APP_URL = (
    "https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/image.ncl"
)
EXPECTED_VIDEO_APP_URL = (
    "https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/video.ncl"
)
EXPECTED_IMAGE_PLAYGROUND_URL = (
    f"https://ginga.org.br/gingaf/playground/?app={EXPECTED_IMAGE_APP_URL}"
)
EXPECTED_VIDEO_PLAYGROUND_URL = (
    f"https://ginga.org.br/gingaf/playground/?app={EXPECTED_VIDEO_APP_URL}"
)


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


def assert_valid_playground_url(raw_url, expected_app_url):
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
    assert app_url == expected_app_url


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
    assert_valid_playground_url(iframe.get("src", ""), EXPECTED_IMAGE_APP_URL)

    assert len(parser.playground_tabs) == 2
    assert parser.playground_tabs[0].get("aria-selected") == "true"
    assert_valid_playground_url(
        parser.playground_tabs[0].get("data-playground-src", ""),
        EXPECTED_IMAGE_APP_URL,
    )
    assert parser.playground_tabs[1].get("aria-selected") == "false"
    assert_valid_playground_url(
        parser.playground_tabs[1].get("data-playground-src", ""),
        EXPECTED_VIDEO_APP_URL,
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
    assert iframe.get("src") == EXPECTED_IMAGE_PLAYGROUND_URL
    assert_valid_playground_url(iframe.get("src", ""), EXPECTED_IMAGE_APP_URL)
    assert iframe.get("title") is None
    assert iframe.get("loading") == "lazy"
    assert "fullscreen" in iframe.get("allow", "")

    assert len(parser.playground_tabs) == 2
    assert (
        parser.playground_tabs[0].get("data-playground-src")
        == EXPECTED_IMAGE_PLAYGROUND_URL
    )
    assert (
        parser.playground_tabs[1].get("data-playground-src")
        == EXPECTED_VIDEO_PLAYGROUND_URL
    )


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


def _wait_for_playground_app(page, responses, expected_app_url):
    deadline = time.time() + 30
    playground_frame = None
    flutter_ready = False
    ncl_fetched = False

    while time.time() < deadline:
        playground_frame = None
        for frame in page.frames:
            if (
                "ginga.org.br/gingaf/" in frame.url
                and "playground=true" in frame.url
                and parse_qs(urlsplit(frame.url).query).get("app") == [expected_app_url]
            ):
                playground_frame = frame
                break

        ncl_fetched = any(
            status == 200 and resp_url == expected_app_url
            for status, resp_url in responses
        )

        if playground_frame is not None:
            try:
                flutter_ready = playground_frame.evaluate(
                    "() => Boolean(document.querySelector('flutter-view')) && document.title === 'gingaf'"
                )
            except Exception:
                flutter_ready = False

        if playground_frame is not None and flutter_ready and ncl_fetched:
            break

        page.wait_for_timeout(300)

    assert playground_frame is not None, (
        f"Playground iframe did not redirect to gingaf playground mode for {expected_app_url}. "
        f"Frames: {[f.url for f in page.frames]}"
    )
    assert flutter_ready, (
        "Ginga Playground Flutter view did not initialize inside the iframe."
    )
    assert ncl_fetched, (
        f"Expected HTTP 200 fetch of {expected_app_url} inside playground iframe."
    )
    return playground_frame


@pytest.mark.parametrize("lang", LOCALES)
def test_browser_loads_playground_iframe_and_switches_between_image_and_video(
    browser, site_server, lang
):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    responses = []
    page_errors = []
    page.on("response", lambda r: responses.append((r.status, r.url)))
    page.on("pageerror", lambda err: page_errors.append(str(err)))

    try:
        page.goto(
            site_server.url(f"/{lang}/gingancl/handbook/media/"),
            wait_until="domcontentloaded",
            timeout=30000,
        )

        iframe_el = page.locator("iframe.ginga-playground")
        assert iframe_el.count() == 1
        iframe_el.scroll_into_view_if_needed()

        box = iframe_el.bounding_box()
        assert box is not None
        assert box["width"] >= 300
        assert box["height"] >= 500

        playground_frame = _wait_for_playground_app(
            page, responses, EXPECTED_IMAGE_APP_URL
        )

        flutter_box = playground_frame.evaluate(
            """() => {
                const el = document.querySelector('flutter-view');
                if (!el) return null;
                const r = el.getBoundingClientRect();
                return { width: r.width, height: r.height };
            }"""
        )
        assert flutter_box is not None
        assert flutter_box["width"] >= 300
        assert flutter_box["height"] >= 500

        if lang == "en":
            tabs = page.locator("button.ginga-playground-tab")
            assert tabs.count() == 2
            assert tabs.nth(0).inner_text().strip() == "image.ncl"
            assert tabs.nth(1).inner_text().strip() == "video.ncl"
            tabs.nth(1).click()
            assert tabs.nth(0).get_attribute("aria-selected") == "false"
            assert tabs.nth(1).get_attribute("aria-selected") == "true"
            assert iframe_el.get_attribute("src") == EXPECTED_VIDEO_PLAYGROUND_URL
            _wait_for_playground_app(page, responses, EXPECTED_VIDEO_APP_URL)

        assert page_errors == []
    finally:
        context.close()

