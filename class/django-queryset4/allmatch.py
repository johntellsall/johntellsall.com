
import fileinput
import re

word_pat = re.compile('\w+')

for line in fileinput.input():
    for match in word_pat.finditer(line):
        print match.group(0)