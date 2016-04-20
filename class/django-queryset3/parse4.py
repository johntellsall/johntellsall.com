# 4. dictionary
import fileinput, re
from itertools import *
def has_comment(line):
    return line.startswith('#')
def parse_keyvalue(line):
    m = re.match(r'(\S+):(.+)', line)
    if m:
        return m.groups()
    return None
lines = ifilterfalse(has_comment, fileinput.input())
matches = (parse_keyvalue(line) for line in lines)
keyvalues = ifilter(None, matches)
confdict = dict(keyvalues)
print confdict
