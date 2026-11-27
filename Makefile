.PHONY: help deps test build build-playground serve zip deploy-folder analytics clean

CATALOG_URL ?= https://raw.githubusercontent.com/ginga-org-br/gingaf/refs/heads/main/examples/catalog.json
LOCAL_CATALOG ?= ../gingaf/examples/catalog.json

help:
	@echo "Available Makefile targets:"
	@echo "  help             - Show this help message"
	@echo "  deps             - Setup project and install dependencies"
	@echo "  test             - Run unit tests"
	@echo "  build-playground - Generate NCL handbook playground embeds from catalog.json"
	@echo "  build            - Build the site"
	@echo "  serve            - Serve the site locally with a development server"
	@echo "  zip              - Build and package site directory into site.zip"
	@echo "  deploy-folder    - Deploy site to destination via rsync"
	@echo "  analytics        - Open Google Analytics statistics in browser"
	@echo "  clean            - Cleanup built site and cache files"

deps:
	pip install zensical pytest playwright
	python -m playwright install chromium

test:
	python -m pytest

build-playground:
	python scripts/build_playground.py --catalog-url "$(CATALOG_URL)" --local-catalog "$(LOCAL_CATALOG)"

build:
	python -m zensical build

zip: build-playground build
	python -c "import shutil; shutil.make_archive('site', 'zip', 'site')"

deploy-folder: build test
	python scripts/deploy_folder.py "$(GINGA_ORG_DEPLOY)"

clean:
	rm -rf site/
	rm -rf .cache/
	rm -f site.zip

serve:
	zensical serve
