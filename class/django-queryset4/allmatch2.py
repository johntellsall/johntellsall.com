
import fileinput
import re

word_pat = re.compile(r'\w+')

print ''.join(
    match.group(0)
    for line in fileinput.input()
    for match in word_pat.finditer(line))
    
    
        