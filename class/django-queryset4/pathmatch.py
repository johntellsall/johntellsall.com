
import re

number_pat = re.compile('[0-9.]+')

print '\n'.join(
    match.group(0)
    for match in number_pat.finditer(line)
    for line in open('recipe.ini')
    )