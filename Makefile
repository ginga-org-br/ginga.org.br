.PHONY: help deps serve build build-playground zip clean

help:
	@echo "Available Makefile targets:"
	@echo "  help      - Show this help message"
	@echo "  deps      - Setup project and install dependencies"
	@echo "  build     - Build the site"
	@echo "  serve     - Serve the site locally with a development server"
	@echo "  zip       - Build and package site directory into site.zip"
	@echo "  clean     - Cleanup built site and cache files"

deps:
	pip install zensical

build:
	zensical build

zip: build build-playground
	python -c "import shutil; shutil.make_archive('site', 'zip', 'site')"

clean:
	rm -rf site/
	rm -rf .cache/
	rm -f site.zip

serve: 
	zensical serve	