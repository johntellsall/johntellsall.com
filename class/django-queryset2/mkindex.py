#!/usr/bin/env python

import fileinput, re

title_pat = re.compile(r'[=-]{5}')
iter_pat = re.compile('(iter)', re.IGNORECASE)
queryset_pat = re.compile('(queryset)', re.IGNORECASE)
funcprog_pat = re.compile('(fp|functional)', re.IGNORECASE)

def parse_section(title):
    if funcprog_pat.search(title):
        return 'FP'
    elif queryset_pat.search(title):
        return 'QS'
    elif iter_pat.search(title):
        return 'iter'
    return None

prev_line = None
page_num = 0
section = None
for num,line in enumerate(fileinput.input()):
    if title_pat.match(line):
        page_num += 1
        if page_num > 2:
            section = parse_section(prev_line) or section
        print '{:3d} {:4}'.format(page_num, section or '-'),
        if '-' in line:
            print ' '*4,
        print prev_line,
    prev_line = line

    
