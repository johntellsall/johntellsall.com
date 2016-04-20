# 2. stream of valid lines
import fileinput
from itertools import *
def has_comment(line):
    return line.startswith('#')
def has_keyvalue(line):
    return ':' in line
lines = ifilterfalse( has_comment, fileinput.input() )
lines = ifilter( has_keyvalue, lines )
print ''.join( lines )
