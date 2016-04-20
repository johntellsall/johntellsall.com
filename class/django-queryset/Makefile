all:	jslides

include dev.mk
include hieroglyph.mak

start:
	./project/project/manage.py runserver

%.html: %.py
	pygmentize -f html $< > $@

jslides:
	sphinx-build -qN -b slides -d _build/doctrees \
	-D slide_theme=single-level \
	. _build/slides
	@echo
	@wc -l *.rst

# 	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) $(BUILDDIR)/slides


