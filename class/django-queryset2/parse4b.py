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
confdict = dict(
    kv for kv in (
        parse_keyvalue(line)
        for line in fileinput.input()
    ) if kv
    )
print confdict
