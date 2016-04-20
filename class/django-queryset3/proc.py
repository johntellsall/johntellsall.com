# proc.py: procedural config parser
import fileinput, re
mydict = {}
for line in fileinput.input():
    if line.startswith('#'):
        continue
    m = re.match(r'(\S+):(.+)', line)
    if not m:
        continue
    key,value = m.groups()
    mydict[key] = value
print mydict
