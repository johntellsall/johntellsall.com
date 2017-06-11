export PATH := /home/johnm/local/bin/:$(PATH)

all:

# zap-config:
# 	-$(RM) mycontainer/config.json

# XX must be run as root!
# [ "$output" = "uid=0(root) gid=0(root)" ]
.ONESHELL:
c-id:
	cd mycontainer
	-$(RM) config.json
	runc spec
	sed -ie 's/"terminal": true,//' config.json
	sed -ie 's/"sh"/"sh", "-c", "id"/' config.json
	runc run c-id
