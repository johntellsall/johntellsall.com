"""
example2.py -- parse CSV file
"""


def parse_lines(lines):
    result = []
    for line in lines:
        result.append(line.split(','))
    return result


def main():
    recipe = open('oldfashioned.csv').readlines()
    out = parse_lines(recipe)
    for line in out:
        print(line)

if __name__ == '__main__':
    main()
