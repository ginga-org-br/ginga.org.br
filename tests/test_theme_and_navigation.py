from html.parser import HTMLParser
import json
import posixpath
import re
import subprocess
import unittest
from urllib.parse import urlsplit

from site_test_utils import DOCS_DIR, LOCALES, SITE_DIR, ensure_site_built


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


class HeaderParser(HTMLParser):
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


class TestThemeAndNavigation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ensure_site_built()

    def test_primary_sidebar_is_scoped_to_active_language(self):
        for lang in LOCALES:
            with self.subTest(lang=lang):
                html = (SITE_DIR / lang / "index.html").read_text(encoding="utf-8")
                parser = PrimaryNavParser()
                parser.feed(html)

                other_langs = tuple(l for l in LOCALES if l != lang)
                self.assertGreater(len(parser.nav_links), 20)

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
                        self.assertFalse(
                            resolved == other or resolved.startswith(f"{other}/"),
                            f"Sidebar on /{lang}/ leaked link '{href}' resolving to '{resolved}'",
                        )

    def test_handbook_xml_tag_titles_are_escaped_in_navigation(self):
        critical_tags = ("area", "body", "head", "link", "media", "meta")
        for lang in LOCALES:
            with self.subTest(lang=lang):
                html = (SITE_DIR / lang / "index.html").read_text(encoding="utf-8")
                match = re.search(
                    r'<nav class="md-nav md-nav--primary".*?</nav>\s*</div>',
                    html,
                    re.S,
                )
                self.assertIsNotNone(match)
                nav_html = match.group(0)
                for tag_name in critical_tags:
                    with self.subTest(lang=lang, tag=tag_name):
                        self.assertIn(f"&lt;{tag_name}&gt;", nav_html)
                        self.assertNotRegex(
                            nav_html,
                            rf'<span class="md-ellipsis">\s*<{tag_name}>\s*</span>',
                        )

    def test_header_includes_playground_button_and_language_switcher(self):
        for lang in LOCALES:
            with self.subTest(lang=lang):
                html = (SITE_DIR / lang / "index.html").read_text(encoding="utf-8")
                parser = HeaderParser()
                parser.feed(html)

                playground_links = [
                    a
                    for a in parser.header_links
                    if "md-playground-button" in a.get("class", "").split()
                ]
                self.assertEqual(len(playground_links), 1)
                btn = playground_links[0]
                self.assertEqual(btn.get("href"), "/gingaf/playground/")
                self.assertEqual(btn.get("target"), "_blank")
                rel_tokens = set(btn.get("rel", "").split())
                self.assertIn("noopener", rel_tokens)
                self.assertIn("noreferrer", rel_tokens)

                alt_hrefs = {
                    a.get("href")
                    for a in parser.header_links
                    if "md-select__link" in a.get("class", "").split()
                }
                self.assertEqual(alt_hrefs, {"/pt/", "/en/", "/es/"})

    def test_root_index_contains_language_redirect_and_noscript_fallback(self):
        root_html = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        self.assertIn("navigator.languages", root_html)
        self.assertIn("startsWith('pt')", root_html)
        self.assertIn("startsWith('es')", root_html)
        self.assertIn("startsWith('en')", root_html)
        self.assertIn('window.location.replace("./" + targetLang + "/")', root_html)
        self.assertIn("<noscript>", root_html)
        self.assertIn('content="0; url=./en/"', root_html)

    def test_worker_postmessage_filters_by_locale_and_escapes_xml_tags(self):
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
        self.assertEqual(len(en_items), 2)
        self.assertEqual(en_items[0]["title"], "&lt;media&gt;")
        self.assertEqual(en_items[0]["path"], ["English", "&lt;media&gt;"])
        self.assertEqual(en_items[1]["title"], "Intro")
        self.assertEqual(result["en"][1], {"type": 1, "data": {"query": "media"}})

        pt_items = result["pt"][0]["data"]["items"]
        self.assertEqual([i["location"] for i in pt_items], ["pt/gingancl/handbook/media/"])
        self.assertEqual(pt_items[0]["title"], "&lt;media&gt;")

        es_items = result["es"][0]["data"]["items"]
        self.assertEqual([i["location"] for i in es_items], ["es/gingancl/handbook/area/"])
        self.assertEqual(es_items[0]["title"], "&lt;area&gt;")

        self.assertEqual(len(result["docFallbackEn"][0]["data"]["items"]), 2)
        self.assertEqual(
            [i["location"] for i in result["docFallbackEs"][0]["data"]["items"]],
            ["es/gingancl/handbook/area/"],
        )
        self.assertEqual(
            [i["location"] for i in result["defaultFallback"][0]["data"]["items"]],
            ["pt/gingancl/handbook/media/"],
        )

    def test_fetch_interceptor_filters_search_json_and_handles_edge_cases(self):
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

        self.assertEqual(len(result["byString"]["items"]), 1)
        self.assertEqual(result["byString"]["items"][0]["location"], "en/gingancl/handbook/body/")
        self.assertEqual(result["byString"]["items"][0]["title"], "&lt;body&gt;")
        self.assertEqual(result["byString"]["items"][0]["path"], ["English", "&lt;body&gt;"])

        self.assertEqual(len(result["byRequestObj"]["items"]), 1)
        self.assertEqual(result["byRequestObj"]["items"][0]["location"], "en/gingancl/handbook/body/")

        self.assertEqual(result["untouched"], {"untouched": True})
        self.assertEqual(result["brokenFallbackBody"], "not-valid-json")


if __name__ == "__main__":
    unittest.main()
