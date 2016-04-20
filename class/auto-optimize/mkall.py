#!/usr/bin/env python

import os, subprocess, sys

for path in sys.argv[1:]:
    outpath = os.path.join(os.path.splitext(path)[0], '.out')
    assert not subprocess.call(
        'env PYTHONPATH=/usr/lib/python2.7/dist-packages/'
        ' python {} > {}'.format(path, outpath)
        )
    

