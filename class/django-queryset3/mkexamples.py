#!/usr/bin/env python

import subprocess, sys

def print_indent(lines):
    for line in lines:
        line = line.rstrip()
        print "    ",line

for path in sys.argv[1:]:
    print path
    print '----------------'
    print
    print '.. code-block:: python'
    print
    print_indent( open(path) )
    print
    print '::'
    print
    output = subprocess.check_output(
        ['python', path, 'recipe.ini']
        ).split('\n')
    print_indent( output )
