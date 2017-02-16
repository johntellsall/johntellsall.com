#!/usr/bin/env python

'''
checkusage.py -- show biggest processes on system
'''

import argparse
import operator
import subprocess


def parse(ps):
    lines = ps.split('\n')
    for line in lines:
        if not line:
            continue
        pcpu, rss, command = line.split(None, 2)
        usage = int(float(pcpu) * int(rss) / 100.)
        yield {'usage': usage, 'command': command}


def test_parse():
    ps_text = ''' 7.0 217720 chrome
 1.8 721324 Web Content
'''
    assert list(parse(ps_text)) == [
        {'command': 'chrome', 'usage': 15240},
        {'command': 'Web Content', 'usage': 12983}]


def run(args):
    ps_bytes = subprocess.check_output(
        'ps -e -o pcpu,rss,comm --no-headers --sort=-pcpu | head',
        shell=True)
    ps_lines = list(parse(ps_bytes.decode()))

    ps_lines = sorted(ps_lines, key=operator.itemgetter('usage'),
        reverse=True)  # noqa
    print(ps_lines)


def main():
    parser = argparse.ArgumentParser()
    run(parser.parse_args())

if __name__ == '__main__':
    main()
