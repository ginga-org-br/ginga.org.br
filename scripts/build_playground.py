import argparse
import json
import os
from pathlib import Path
import re
import urllib.request


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DOCS_DIR = ROOT_DIR / "docs"
DEFAULT_CATALOG_URL = (
    "https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/catalog.json"
)
DEFAULT_LOCAL_CATALOG = ROOT_DIR.parent / "gingaf" / "examples" / "catalog.json"
EXAMPLES_BASE_URL = (
    "https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples"
)
PLAYGROUND_BASE_URL = "https://ginga.org.br/gingaf/playground/"
NON_ELEMENT_FILES = {"about.md", "footer.md"}

I18N = {
    "en": (
        "Explore the `<{tag}>` example below:",
        "Explore the `<{tag}>` examples below:",
        "Ginga Playground examples",
    ),
    "pt": (
        "Explore o exemplo de `<{tag}>` abaixo:",
        "Explore os exemplos de `<{tag}>` abaixo:",
        "Exemplos do Ginga Playground",
    ),
    "es": (
        "Explore el ejemplo de `<{tag}>` a continuación:",
        "Explore los ejemplos de `<{tag}>` a continuación:",
        "Ejemplos de Ginga Playground",
    ),
}

BLOCK_RE = re.compile(
    r'\n+Explore [^\n]+:\n+<div class="ginga-playground-container">.*?</div>\n+',
    re.S,
)
H1_RE = re.compile(r"(^# [^\n]+\n)", re.M)
TAG_RE = re.compile(r"&lt;([A-Za-z0-9]+)&gt;")


def has_ginga_org_tags(catalog_data):
    if not isinstance(catalog_data, dict):
        return False
    examples = catalog_data.get("examples", {})
    if not isinstance(examples, dict):
        return False
    return any(
        isinstance(entry, dict) and bool(entry.get("ginga.org.br"))
        for entry in examples.values()
    )


def load_catalog(catalog_url=DEFAULT_CATALOG_URL, local_catalog=DEFAULT_LOCAL_CATALOG):
    local_path = Path(local_catalog) if local_catalog else None
    if (
        catalog_url == DEFAULT_CATALOG_URL
        and local_path
        and local_path.is_file()
    ):
        return json.loads(local_path.read_text(encoding="utf-8"))

    if catalog_url:
        try:
            req = urllib.request.Request(
                catalog_url, headers={"User-Agent": "ginga.org.br-build"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw = resp.read().decode("utf-8")
            remote_data = json.loads(raw)
            if has_ginga_org_tags(remote_data) or not (
                local_path and local_path.is_file()
            ):
                return remote_data
        except Exception:
            if not (local_path and local_path.is_file()):
                raise

    if local_path and local_path.is_file():
        return json.loads(local_path.read_text(encoding="utf-8"))

    raise FileNotFoundError(
        f"Unable to load catalog from {catalog_url} or {local_catalog}"
    )


def is_priority_example(info):
    main_file = (info.get("mainFile") or "").strip().lstrip("/")
    return (
        info.get("category") == "ginga.org.br"
        or main_file.startswith("ginga.org.br/")
    )


def group_examples_by_element(catalog_data):
    raw_by_slug = {}
    canon_tag = {}
    examples = catalog_data.get("examples", {})
    if not isinstance(examples, dict):
        return {}, canon_tag

    for info in examples.values():
        if not isinstance(info, dict):
            continue
        tags = info.get("ginga.org.br") or []
        main_file = (info.get("mainFile") or "").strip()
        if not tags or not main_file:
            continue
        rank = 0 if is_priority_example(info) else 1
        for raw_tag in tags:
            tag_str = str(raw_tag).strip()
            if not tag_str:
                continue
            slug = tag_str.lower()
            canon_tag.setdefault(slug, tag_str)
            raw_by_slug.setdefault(slug, []).append((rank, main_file))

    by_slug = {
        slug: [mf for _, mf in sorted(items, key=lambda pair: pair[0])]
        for slug, items in raw_by_slug.items()
    }
    return by_slug, canon_tag


def build_tabs(main_files, examples_base=EXAMPLES_BASE_URL, playground_base=PLAYGROUND_BASE_URL):
    file_parts = [mf.partition("?")[0].lstrip("/") for mf in main_files]
    tabs = []
    for mf, fp in zip(main_files, file_parts):
        _, _, query = mf.partition("?")
        app_url = f"{examples_base}/{fp}"
        pg_url = f"{playground_base}?app={app_url}" + (f"&{query}" if query else "")
        bn = os.path.basename(fp)
        is_dup = sum(1 for item in file_parts if os.path.basename(item) == bn) > 1
        label = fp if (bn in ("main.ncl", "main.ncl360", "main.html") or is_dup) else bn
        tabs.append((label, pg_url))
    return tabs


def render_playground_block(tag_name, tabs, one_tpl, many_tpl, aria_label):
    intro = (many_tpl if len(tabs) > 1 else one_tpl).format(tag=tag_name)
    buttons = "\n".join(
        f'  <button type="button" class="ginga-playground-tab" role="tab" '
        f'aria-selected="{"true" if idx == 0 else "false"}" '
        f'data-playground-src="{url}">{label}</button>'
        for idx, (label, url) in enumerate(tabs)
    )
    first_url = tabs[0][1]
    return (
        f"\n{intro}\n\n"
        f'<div class="ginga-playground-container">\n\n'
        f'<nav class="ginga-playground-tabs" role="tablist" aria-label="{aria_label}">\n'
        f"{buttons}\n"
        f"</nav>\n\n"
        f"<iframe\n"
        f'  class="ginga-playground"\n'
        f'  src="{first_url}"\n'
        f'  loading="lazy"\n'
        f'  allow="autoplay; fullscreen">\n'
        f"</iframe>\n\n"
        f"</div>\n\n"
    )


def sync_handbook_playgrounds(catalog_data, docs_dir=DEFAULT_DOCS_DIR):
    docs_root = Path(docs_dir)
    by_slug, canon_tag = group_examples_by_element(catalog_data)
    updated = 0

    for lang, (one_tpl, many_tpl, aria_label) in I18N.items():
        handbook_dir = docs_root / lang / "gingancl" / "handbook"
        if not handbook_dir.is_dir():
            continue
        for md_path in sorted(handbook_dir.glob("*.md")):
            if md_path.name in NON_ELEMENT_FILES:
                continue
            slug = md_path.stem.lower()
            main_files = by_slug.get(slug, [])
            text = md_path.read_text(encoding="utf-8")
            cleaned = BLOCK_RE.sub("\n\n", text)

            if not main_files:
                if cleaned != text:
                    md_path.write_text(cleaned, encoding="utf-8")
                    updated += 1
                continue

            m_h1 = H1_RE.search(cleaned)
            if not m_h1:
                continue

            m_tag = TAG_RE.search(cleaned)
            tag_name = m_tag.group(1) if m_tag else canon_tag.get(slug, slug)
            tabs = build_tabs(main_files)
            widget = render_playground_block(
                tag_name, tabs, one_tpl, many_tpl, aria_label
            )

            pos = m_h1.end()
            rest = cleaned[pos:].lstrip("\n")
            new_text = cleaned[:pos] + widget + rest
            if new_text != text:
                md_path.write_text(new_text, encoding="utf-8")
                updated += 1

    return updated


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-url", default=DEFAULT_CATALOG_URL)
    parser.add_argument("--local-catalog", default=str(DEFAULT_LOCAL_CATALOG))
    parser.add_argument("--docs-dir", default=str(DEFAULT_DOCS_DIR))
    args = parser.parse_args(argv)

    catalog_data = load_catalog(args.catalog_url, args.local_catalog)
    updated = sync_handbook_playgrounds(catalog_data, args.docs_dir)
    print(f"Updated {updated} handbook files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
