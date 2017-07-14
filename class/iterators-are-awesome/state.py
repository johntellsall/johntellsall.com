import os
import tempfile


class State:

    def __init__(self, path):
        self.path = path

    def fetch(self):
        with open(self.path) as state_fh:
            return state_fh.read()

    def update(self, value):
        with open(self.path, 'w') as state_fh:
            state_fh.write(value)

    def delete(self):
        os.remove(self.path)


def test_happy_path():
    path = tempfile.NamedTemporaryFile().name
    try:
        s = State(path)
        s.update('123')
        assert s.fetch() == '123'
        s.delete()
        assert not os.path.exists(path)
    finally:
        if os.path.isfile(path):
            os.remove(path)
