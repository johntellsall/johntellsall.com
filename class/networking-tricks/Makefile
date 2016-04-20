all: single jslides

# Hieroglyph: -j9=parallel, -n=nitpicky, -b=use single builder,
# -N=no colors;
# then: sourcedir builddir sourcefiles
.PHONY: single
single:
	@egrep '====' index.rst | wc -l
	@echo
	sphinx-build -j9 -n -N -b singlehtml \
	. _build/singlehtml index.rst \
	2>&1 | egrep -v 'any doctree'

.PHONY: jslides
jslides: index.rst
	sphinx-build -qN -b slides -d _build/doctrees \
	. _build/slides

# info:
# 	wc -l *.rst



# zoot:
# 		sphinx-build -b singlehtml \
# 		. _build/singlehtml 


 ::::::::::::::::::::::::: DEV

# INSTALL: pip install watchdog
automake:
		watchmedo shell-command \
		--pattern='*.rst' --command 'make all'



# :::::::::::::::::::::::::::::::::::::::: PUSH

WEB := $(HOME)/src/johntellsall/website/networking-tricks

# copy all but backup files and output files, like '_build'
push:
	-ln -s $(PWD)/_build/slides .
	rsync -sva --copy-links \
	`/bin/ls -1 | egrep -v '[_~]'` $(WEB)/
	@echo
	find $(WEB) -type f
