"""
example2.py -- parse CSV file
"""


import sys


def parse_lines(lines):
    result = []
    for line in lines:
        fields = line.rstrip('\n').split(',')
        result.append(fields)
    return result


def main(path):
    recipe = open(path).readlines()
    out = parse_lines(recipe)
    for fields in out:
        print(fields)

if __name__ == '__main__':
    main(sys.argv[1])


def test_parse_lines():
    assert parse_lines(['cat,dog']) == [['cat', 'dog']]

def test_parse_lines_strip_newline():
    assert parse_lines([r'dog\n']) == [['dog']]
