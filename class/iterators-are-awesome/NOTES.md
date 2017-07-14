def get_paths(topdir):
    for dirpath, _, files in os.walk(topdir):
        yield from (os.path.join(dirpath, name) for name in files)


# virtualenv -p python3 venv
python3 -m venv venv
. ./venv/bin/activate
