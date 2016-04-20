tags:
	ctags-exuberant -e -R --languages=python \
	. $(VIRTUAL_ENV)/lib/python*/*/django
	wc -l TAGS
