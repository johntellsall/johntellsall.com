"""
example2.py -- parse CSV file
"""


def parse_lines(lines):
    result = []
    for line in lines:
        fields = line.rstrip('\n').split(',')
        result.append(fields)
    return result


def main():
    recipe = open('oldfashioned.csv').readlines()
    out = parse_lines(recipe)
    for line in out:
        print(line)

if __name__ == '__main__':
    main()


def test_parse_lines():
    assert parse_lines('cat,dog') == 'blam'

