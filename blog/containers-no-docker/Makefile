export PATH := /home/johnm/local/bin/:$(PATH)

all:

zap-config:
	-$(RM) mycontainer/config.json

.ONESHELL:
c-id: zap-config
	cd mycontainer
	runc spec
	sed -ie 's/"terminal": true,//' config.json
	sed -ie 's/"sh"/"sh", "-c", "id"/' config.json
	runc run c-id
