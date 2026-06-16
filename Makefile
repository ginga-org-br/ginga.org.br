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

build-playground:
	python -c "import os, subprocess; subprocess.run(['$(MAKE)', '-C', '../gingaf/playground', 'build']) if not os.path.exists('../gingaf/playground/dist') else None"
	python -c "import os, shutil; shutil.copytree('../gingaf/playground/dist', 'site/playground', dirs_exist_ok=True) if os.path.exists('../gingaf/playground/dist') else None; shutil.copytree('../gingaf/ginga/build/web', 'site/playground/player', dirs_exist_ok=True) if os.path.exists('../gingaf/ginga/build/web') else None; [(lambda p, c=open(p).read(): open(p, 'w').write(c.replace('/gingaf/', '/')))(p) for p in ['site/playground/index.html', 'site/playground/player/index.html'] if os.path.exists(p)]"
	python -c "import shutil; shutil.copy2('docs/index.html', 'site/index.html')"

zip: build build-playground
	python -c "import shutil; shutil.make_archive('site', 'zip', 'site')"

clean:
	rm -rf site/
	rm -rf .cache/
	rm -f site.zip

serve: 
	@python -c "import socket, random, subprocess, sys; port = next(p for p in random.sample(range(8001, 9000), 999) if socket.socket().connect_ex(('127.0.0.1', p)) != 0); print(f'Serving on http://localhost:{port}', flush=True); subprocess.run(['zensical', 'serve', '-a', f'127.0.0.1:{port}'])"