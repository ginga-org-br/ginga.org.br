.PHONY: help deps serve build test clean

help:
	@echo "Available Makefile targets:"
	@echo "  help      - Show this help message"
	@echo "  deps      - Setup project and install dependencies"
	@echo "  build     - Build all localized versions of the site"
	@echo "  test      - Build and verify multi-locale output site structure"
	@echo "  serve     - Serve the built en site locally with a development server"
	@echo "  serve-all - Serve the built en,es,pt site locally with a development server"
	@echo "  clean     - Cleanup built site and cache files"

deps:
	pip install zensical

build:
	python -c "import shutil; shutil.rmtree('docs/en/assets', ignore_errors=True); shutil.rmtree('docs/pt/assets', ignore_errors=True); shutil.rmtree('docs/es/assets', ignore_errors=True)"
	python -c "import shutil; shutil.copytree('docs/assets', 'docs/en/assets', dirs_exist_ok=True); shutil.copytree('docs/assets', 'docs/pt/assets', dirs_exist_ok=True); shutil.copytree('docs/assets', 'docs/es/assets', dirs_exist_ok=True)"
	zensical build -f zensical.en.toml --clean
	zensical build -f zensical.pt.toml --clean
	zensical build -f zensical.es.toml --clean
	python -c "import shutil; shutil.copy2('docs/index.html', 'site/index.html')"

test: build
	python -c "import os, sys; paths = ['site/index.html', 'site/en/index.html', 'site/pt/index.html', 'site/es/index.html']; missing = [p for p in paths if not os.path.exists(p) or os.path.getsize(p) == 0]; sys.exit(1) if missing else print('All site build targets verified successfully.')"

clean:
	rm -rf site/
	rm -rf .cache/

serve: 
	zensical serve -f zensical.en.toml

serve-all: build
	@python -c "exec(\"import sys, subprocess\nport = next(p for p in range(8000, 9000) if (lambda s: (res := s.connect_ex(('127.0.0.1', p)), s.close(), res != 0)[2])(__import__('socket').socket()))\nprint(f'http://localhost:{port}', flush=True)\ntry: subprocess.run([sys.executable, '-m', 'http.server', '--directory', 'site', str(port)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)\nexcept KeyboardInterrupt: pass\")"