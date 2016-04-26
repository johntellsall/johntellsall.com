import re

def ing_name(ing):
    return ing.group('name')

def parse_ing(line):
    return re.match(r'[0-9].+\s(?P<name>\w+)', line)

print '\n'.join(
    ing_name(ing)
    parse_ing(line)
    for line in open('oldfashioned.ini')
        )
