export PATH := /home/johnm/local/bin/:$(PATH)

all:

# zap-config:
# 	-$(RM) mycontainer/config.json

# XX must be run as root!
# [ "$output" = "uid=0(root) gid=0(root)" ]
.ONESHELL:
c-root:
	cd mycontainer
	-$(RM) config.json
	runc spec
	sed -ie 's/"terminal": true,//' config.json
	sed -ie 's/"sh"/"sh", "-c", "id"/' config.json
	runc run c-id

# c-user: rootless/user container, don't need root!
.ONESHELL:
c-user:
	cd mycontainer
	-$(RM) config.json
	runc spec --rootless
	sed -ie 's/"terminal": true,//' config.json
	sed -ie 's/"sh"/"sh", "-c", "id"/' config.json
	runc run c-id
# XXXX

# container_linux.go:265: starting container process caused
# "process_linux.go:347: container init caused \"rootfs_linux.go:135:
# setting rootfs as readonly caused \\\"operation not permitted\\\"\""


# 	runc run --root /tmp/runc c-id

# "runc spec --rootless" requires recompile
# Easiest: "make dbuild && mv ./runc ~/local/bin/"
