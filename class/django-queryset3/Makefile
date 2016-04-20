WEB := $(HOME)/src/johntellsall/website/class/django-queryset2

all: jslides

# copy all but backup files and output files, like '_build'
push:
	-ln -s $(PWD)/_build/slides .
	rsync -sva --copy-links \
	`/bin/ls -1 | egrep -v '[_~]'` $(WEB)/
	@echo
	find $(WEB) -type f

count: fp-examples.rst
	cat index.rst fp-examples.rst | ./mkindex.py -

%.rst: %.py
	./mkexamples.py $<

last.out:
	make `ls -1t *.py | head -1 | sed -e s/.py/.out/`

.PHONY: fp-examples.rst
fp-examples.rst:
	./mkexamples.py parse?.py > $@

oindex:
	./mkindex.py ../django-queryset/index.rst

jslides: fp-examples.rst
	sphinx-build -qN -b slides -d _build/doctrees \
	-D slide_theme=single-level \
	. _build/slides
	@echo
	wc -l *.rst


tags:
	ctags-exuberant -e -R --languages=python \
	. $(VIRTUAL_ENV)/lib/python*/*/django
	wc -l TAGS

images:
	/bin/ls -1 _static/*g \
	| awk '{print ".. image::",$$1}'
# .. image:: _static/large_BaxterCutawayFF3.jpg
