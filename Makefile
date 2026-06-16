.PHONY: help deps test build serve zip deploy-folder analytics clean

help:
	@echo "Available Makefile targets:"
	@echo "  help          - Show this help message"
	@echo "  deps          - Setup project and install dependencies"
	@echo "  build         - Build the site"
	@echo "  serve         - Serve the site locally with a development server"
	@echo "  zip           - Build and package site directory into site.zip"
	@echo "  deploy-folder - Deploy site to destination via rsync"
	@echo "  analytics     - Open Google Analytics statistics in browser"
	@echo "  clean         - Cleanup built site and cache files"

deps:
	pip install zensical

build:
	zensical build

zip: build build-playground
	python -c "import shutil; shutil.make_archive('site', 'zip', 'site')"

deploy-folder: build
	$(if $(strip $(GINGA_ORG_DEPLOY)),,$(error GINGA_ORG_DEPLOY is not set))
	@target_dir="$$(realpath -m "$(GINGA_ORG_DEPLOY)")"; \
	mounted=0; \
	curr="$$target_dir"; \
	while [ "$$curr" != "/" ] && [ -n "$$curr" ]; do \
		if mountpoint -q "$$curr" 2>/dev/null; then \
			mounted=1; \
			mount_dir="$$curr"; \
			break; \
		fi; \
		curr="$$(dirname "$$curr")"; \
	done; \
	if [ "$$mounted" -eq 0 ]; then \
		printf "\033[0;31mError: %s is not mounted (remote FTPES mount not detected).\033[0m\n" "$(GINGA_ORG_DEPLOY)"; \
		exit 1; \
	fi; \
	fstype="$$(findmnt -n -o FSTYPE "$$mount_dir" 2>/dev/null)"; \
	case "$$fstype" in \
		*fuse*|*rclone*|*ftp*) ;; \
		*) printf "\033[0;33mWarning: %s filesystem type is '%s' (expected remote FTPES / rclone).\033[0m\n" "$$mount_dir" "$$fstype";; \
	esac
	rsync -rlptcO --delete-after --inplace --exclude '/gingaf' --out-format="%o %n" site/ $(GINGA_ORG_DEPLOY)
	@printf "\033[0;32mDeployment completed successfully.\033[0m\n"

clean:
	rm -rf site/
	rm -rf .cache/
	rm -f site.zip

serve:
	zensical serve
