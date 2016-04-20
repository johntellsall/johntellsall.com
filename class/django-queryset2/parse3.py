# 3. stream of key-value match objects
import fileinput, re
from itertools import *
def has_comment(line):
    return line.startswith('#')
def parse_keyvalue(line):
    m = re.match(r'(\S+):(.+)', line)
    if m:
        return m.groups()
    return None
matches = (parse_keyvalue(line) for line in fileinput.input())
keyvalues = ifilter(None, matches)
print '\n'.join( (str(kv) for kv in keyvalues) )
