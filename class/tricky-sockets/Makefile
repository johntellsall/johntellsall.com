SHELL := /bin/bash

all: single # jslides

sendmsg:
	find . -name '*.c' | xargs egrep -q sendmsg | egrep -v zmq


count:
	/bin/echo index.rst wrong.rst tricks.rst awesome.rst \
	| xargs wc -l

%.src: %.py
	python $< > $@

%.out: %.py
	python $< > $@

%.html: %.py
	pygmentize -f html $< > $@

# :::::::::::::::::::::::::::::::::::::::: PUSH

WEB := $(HOME)/src/johntellsall/website/class/tricky-sockets

# copy all but backup files and output files, like '_build'
push:
	-ln -s $(PWD)/_build/slides .
	rsync -sva --copy-links \
	`/bin/ls -1 | egrep -v '[_~]'` $(WEB)/
	@echo
	find $(WEB) -type f

# :::::::::::::::::::::::::::::::::::::::: BUILD

# images -- list images in Markdown format
# Ex: .. image:: _static/large_BaxterCutawayFF3.jpg
.PHONY: images
images:
        /bin/ls -1 _static/*g \
        | awk '{print ".. image::",$$1}'


# Hieroglyph: -j9=parallel, -n=nitpicky, -b=use single builder,
# -N=no colors;
# then: sourcedir builddir sourcefiles
.PHONY: single
single:
	sphinx-build -j9 -n -N -b singlehtml \
	. _build/singlehtml index.rst \
	2>&1 | egrep -v 'any doctree'


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
	--pattern='*.rst' --command 'make all'

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS

clean:
	-$(RM) *.gz *.dsc
