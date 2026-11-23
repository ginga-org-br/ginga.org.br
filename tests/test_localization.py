from html.parser import HTMLParser
import json
import posixpath
import subprocess
from urllib.parse import urlsplit

import pytest

from conftest import DOCS_DIR, LOCALES, ROOT_DIR


EXTRA_JS_PATH = DOCS_DIR / "assets" / "javascripts" / "extra.js"


def run_extra_js_scenario(scenario_js):
    driver = f"""
const fs = require('fs');
const vm = require('vm');
const extraCode = fs.readFileSync({json.dumps(str(EXTRA_JS_PATH))}, 'utf8');

async function main() {{
  const result = await (async () => {{
    {scenario_js}
  }})();
  process.stdout.write(JSON.stringify(result));
}}

main().catch((err) => {{
  console.error(err && err.stack ? err.stack : String(err));
  process.exit(1);
}});
"""
    proc = subprocess.run(
        ["node", "-e", driver],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(
            f"Node test scenario failed (exit {proc.returncode}):\n{proc.stderr}\n{proc.stdout}"
        )
    return json.loads(proc.stdout)


class HeaderLinksParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_header = False
        self.header_links = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == "header":
            self.in_header = True
        elif self.in_header and tag == "a":
            self.header_links.append(attr_map)

    def handle_endtag(self, tag):
        if tag == "header":
            self.in_header = False


class PrimaryNavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nav_depth = 0
        self.nav_links = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        classes = set(attr_map.get("class", "").split())
        if tag == "nav":
            if self.nav_depth > 0 or "md-nav--primary" in classes:
                self.nav_depth += 1
        elif self.nav_depth > 0 and tag == "a" and "href" in attr_map:
            self.nav_links.append(attr_map["href"])

    def handle_endtag(self, tag):
        if tag == "nav" and self.nav_depth > 0:
            self.nav_depth -= 1


def test_trilingual_file_parity():
    locale_files = {
        lang: {
            p.relative_to(DOCS_DIR / lang).as_posix()
            for p in (DOCS_DIR / lang).rglob("*.md")
        }
        for lang in LOCALES
    }
    base_files = locale_files["en"]
    assert len(base_files) > 0
    for lang in ("pt", "es"):
        assert sorted(base_files - locale_files[lang]) == [], (
            f"Missing {lang} translations for EN docs"
        )
        assert sorted(locale_files[lang] - base_files) == [], (
            f"Extra {lang} docs not present in EN"
        )


def test_configured_alternates_and_abbreviation_includes(zensical_config):
    alternates = zensical_config["project"].get("extra", {}).get("alternate", [])
    alt_langs = {item["lang"]: item["link"] for item in alternates}
    assert alt_langs == {"pt": "/pt/", "en": "/en/", "es": "/es/"}

    for lang in LOCALES:
        inc_path = ROOT_DIR / "includes" / f"abbreviations_{lang}.md"
        assert inc_path.is_file()
        lines = [
            line.strip()
            for line in inc_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        assert len(lines) > 0
        for line in lines:
            assert line.startswith("*[") and "]:" in line, (
                f"Invalid abbreviation definition in {inc_path.name}: {line}"
            )


def test_root_index_contains_language_redirect_and_noscript_fallback(built_site):
    root_html = (built_site / "index.html").read_text(encoding="utf-8")
    assert "navigator.languages" in root_html
    assert "startsWith('pt')" in root_html
    assert "startsWith('es')" in root_html
    assert "startsWith('en')" in root_html
    assert 'window.location.replace("./" + targetLang + "/")' in root_html
    assert "<noscript>" in root_html
    assert 'content="0; url=./en/"' in root_html


@pytest.mark.parametrize(
    ("browser_locale", "expected_path"),
    [
        ("pt-BR", "/pt/"),
        ("es-ES", "/es/"),
        ("en-US", "/en/"),
        ("fr-FR", "/en/"),
    ],
)
def test_root_language_redirect_by_browser_locale(
    browser, site_server, browser_locale, expected_path
):
    context = browser.new_context(locale=browser_locale)
    page = context.new_page()
    try:
        page.goto(
            site_server.url("/"),
            wait_until="domcontentloaded",
            timeout=15000,
        )
        page.wait_for_url(f"**{expected_path}", timeout=10000)
        assert page.url.endswith(expected_path)
    finally:
        context.close()


def test_header_language_switcher_links_and_navigation(built_site, browser, site_server):
    for lang in LOCALES:
        html = (built_site / lang / "index.html").read_text(encoding="utf-8")
        parser = HeaderLinksParser()
        parser.feed(html)
        alt_hrefs = {
            a.get("href")
            for a in parser.header_links
            if "md-select__link" in a.get("class", "").split()
        }
        assert alt_hrefs == {"/pt/", "/en/", "/es/"}

    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        page.goto(site_server.url("/en/"), wait_until="load", timeout=15000)
        page.locator(".md-select").hover()
        page.locator(".md-select__link[href='/pt/']").click()
        page.wait_for_url("**/pt/", timeout=10000)
        assert page.url.endswith("/pt/")

        page.locator(".md-select").hover()
        page.locator(".md-select__link[href='/es/']").click()
        page.wait_for_url("**/es/", timeout=10000)
        assert page.url.endswith("/es/")
    finally:
        context.close()


@pytest.mark.parametrize("lang", LOCALES)
def test_primary_sidebar_is_scoped_to_active_language(built_site, lang):
    html = (built_site / lang / "index.html").read_text(encoding="utf-8")
    parser = PrimaryNavParser()
    parser.feed(html)

    other_langs = tuple(l for l in LOCALES if l != lang)
    assert len(parser.nav_links) > 20

    for href in parser.nav_links:
        if href.startswith(("#", "http://", "https://")):
            continue
        path = urlsplit(href).path
        if not path:
            continue
        resolved = (
            posixpath.normpath(path.lstrip("/"))
            if path.startswith("/")
            else posixpath.normpath(posixpath.join(lang, path))
        )
        for other in other_langs:
            assert not (resolved == other or resolved.startswith(f"{other}/")), (
                f"Sidebar on /{lang}/ leaked link '{href}' resolving to '{resolved}'"
            )


def test_search_index_covers_all_locales(built_site):
    search_path = built_site / "search.json"
    assert search_path.is_file()
    search_data = json.loads(search_path.read_text(encoding="utf-8"))
    items = search_data.get("items", [])
    assert len(items) > 0

    for lang in LOCALES:
        lang_items = [
            item
            for item in items
            if (item.get("location") or "").startswith(f"{lang}/")
        ]
        assert len(lang_items) > 0


def test_worker_postmessage_filters_by_locale_and_escapes_xml_tags():
    result = run_extra_js_scenario(
        """
        function runCase(pathname, docLang) {
          const sent = [];
          function FakeWorker() {}
          FakeWorker.prototype.postMessage = function (msg) {
            sent.push(msg);
          };
          const sandbox = {
            window: {
              location: { pathname },
              fetch: null,
            },
            document: { documentElement: { lang: docLang } },
            Worker: FakeWorker,
            Response: class FakeResponse {},
          };
          vm.runInNewContext(extraCode, sandbox);

          const w = new FakeWorker();
          w.postMessage({
            type: 0,
            data: {
              items: [
                { location: 'pt/gingancl/handbook/media/', title: '<media>', path: ['Português', '<media>'] },
                { location: 'en/gingancl/handbook/media/', title: '<media>', path: ['English', '<media>'] },
                { location: 'es/gingancl/handbook/area/', title: '<area>', path: ['Español', '<area>'] },
                { location: 'custom-root-match/', title: 'Intro', path: ['English', 'Intro'] },
              ],
            },
          });
          w.postMessage({ type: 1, data: { query: 'media' } });
          return sent;
        }

        return {
          en: runCase('/en/gingancl/handbook/media/', 'pt'),
          pt: runCase('/pt/index.html', 'pt'),
          es: runCase('/es/', 'pt'),
          docFallbackEn: runCase('/', 'en-US'),
          docFallbackEs: runCase('/', 'es-ES'),
          defaultFallback: runCase('/', ''),
        };
        """
    )

    en_items = result["en"][0]["data"]["items"]
    assert len(en_items) == 2
    assert en_items[0]["title"] == "&lt;media&gt;"
    assert en_items[0]["path"] == ["English", "&lt;media&gt;"]
    assert en_items[1]["title"] == "Intro"
    assert result["en"][1] == {"type": 1, "data": {"query": "media"}}

    pt_items = result["pt"][0]["data"]["items"]
    assert [i["location"] for i in pt_items] == ["pt/gingancl/handbook/media/"]
    assert pt_items[0]["title"] == "&lt;media&gt;"

    es_items = result["es"][0]["data"]["items"]
    assert [i["location"] for i in es_items] == ["es/gingancl/handbook/area/"]
    assert es_items[0]["title"] == "&lt;area&gt;"

    assert len(result["docFallbackEn"][0]["data"]["items"]) == 2
    assert [i["location"] for i in result["docFallbackEs"][0]["data"]["items"]] == [
        "es/gingancl/handbook/area/"
    ]
    assert [i["location"] for i in result["defaultFallback"][0]["data"]["items"]] == [
        "pt/gingancl/handbook/media/"
    ]


def test_fetch_interceptor_filters_search_json_and_handles_edge_cases():
    result = run_extra_js_scenario(
        """
        class FakeResponse {
          constructor(body, init) {
            this.body = body;
            this.status = (init && init.status) || 200;
            this.statusText = (init && init.statusText) || 'OK';
            this.headers = (init && init.headers) || {};
          }
          clone() {
            return new FakeResponse(this.body, {
              status: this.status,
              statusText: this.statusText,
              headers: this.headers,
            });
          }
          async json() {
            return JSON.parse(this.body);
          }
        }

        const payload = JSON.stringify({
          items: [
            { location: 'en/gingancl/handbook/body/', title: '<body>', path: ['English', '<body>'] },
            { location: 'pt/gingancl/handbook/body/', title: '<body>', path: ['Português', '<body>'] },
          ],
        });

        const sandbox = {
          window: {
            location: { pathname: '/en/standards/' },
            fetch: async (resource) => {
              const url = typeof resource === 'string' ? resource : resource.url;
              if (url.includes('broken')) {
                return new FakeResponse('not-valid-json', { status: 200 });
              }
              if (url.includes('search.json')) {
                return new FakeResponse(payload, { status: 200 });
              }
              return new FakeResponse(JSON.stringify({ untouched: true }), { status: 200 });
            },
          },
          document: { documentElement: { lang: 'pt' } },
          Response: FakeResponse,
        };

        vm.runInNewContext(extraCode, sandbox);

        const r1 = await sandbox.window.fetch('/search.json');
        const r2 = await sandbox.window.fetch({ url: 'https://ginga.org.br/search.json' });
        const r3 = await sandbox.window.fetch('/assets/other.json');
        const r4 = await sandbox.window.fetch('/broken-search.json');

        return {
          byString: await r1.json(),
          byRequestObj: await r2.json(),
          untouched: await r3.json(),
          brokenFallbackBody: r4.body,
        };
        """
    )

    assert len(result["byString"]["items"]) == 1
    assert result["byString"]["items"][0]["location"] == "en/gingancl/handbook/body/"
    assert result["byString"]["items"][0]["title"] == "&lt;body&gt;"
    assert result["byString"]["items"][0]["path"] == ["English", "&lt;body&gt;"]

    assert len(result["byRequestObj"]["items"]) == 1
    assert result["byRequestObj"]["items"][0]["location"] == "en/gingancl/handbook/body/"

    assert result["untouched"] == {"untouched": True}
    assert result["brokenFallbackBody"] == "not-valid-json"


@pytest.mark.parametrize("lang", LOCALES)
def test_search_filtering_and_xml_tag_escaping_in_browser(browser, site_server, lang):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        page.goto(
            site_server.url(f"/{lang}/"),
            wait_until="load",
            timeout=15000,
        )
        data = page.evaluate(
            """async () => {
                const res = await fetch('/search.json');
                return await res.json();
            }"""
        )
        items = data.get("items", [])
        assert len(items) > 0

        other_langs = tuple(l for l in LOCALES if l != lang)
        for item in items:
            loc = (item.get("location") or "").lower()
            for other in other_langs:
                assert not (loc.startswith(f"{other}/") or f"/{other}/" in loc), (
                    f"Search on /{lang}/ leaked item '{loc}'"
                )

        media_items = [
            item
            for item in items
            if (item.get("location") or "").startswith(
                f"{lang}/gingancl/handbook/media/"
            )
        ]
        assert len(media_items) > 0
        for item in media_items:
            path_items = item.get("path", [])
            assert "&lt;media&gt;" in path_items
            assert "<media>" not in path_items
    finally:
        context.close()


def test_live_search_ui_returns_scoped_results_with_escaped_tags(browser, site_server):
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    try:
        page.goto(site_server.url("/en/"), wait_until="load", timeout=15000)
        page.locator("button.md-search__button").click()
        search_input = page.locator("input[type='text']").first
        search_input.wait_for(state="visible", timeout=5000)
        search_input.fill("media")

        results = []
        for _ in range(25):
            results = search_input.evaluate(
                """el => {
                    const root = el.getRootNode();
                    return Array.from(root.querySelectorAll('a')).map(a => ({
                        href: a.getAttribute('href') || '',
                        text: (a.innerText || '').trim(),
                    }));
                }"""
            )
            if results:
                break
            page.wait_for_timeout(200)

        assert len(results) > 0
        for item in results:
            assert "/en/" in item["href"]
            assert "/pt/" not in item["href"]
            assert "/es/" not in item["href"]

        assert any("<media>" in item["text"] for item in results), (
            f"Expected '<media>' visible in search results, got: {results[:5]}"
        )
    finally:
        context.close()

