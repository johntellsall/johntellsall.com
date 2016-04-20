SHELL := /bin/bash

all:

.PHONY: single
single:
	sphinx-build -b singlehtml -d _build/doctrees \
	. _build/singlehtml

.PHONY: jslides
jslides: index.rst
		sphinx-build -qN -b slides -d _build/doctrees \
		. _build/slides
		@echo
		wc -l *.rst

# ::::::::::::::::::::::::: DEV

# INSTALL: pip install watchdog
automake:
	watchmedo shell-command \
	--pattern='*.rst' --command 'make jslides single'

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS
