#!/usr/bin/env python

def isdata(line):
    return not line.startswith('#')

def amount(line):
    return str(line.split()[:2])

print '\n'.join( map(amount, filter(isdata, open('ing.txt'))) )


print '\n'.join( (
    amount(hasdata)
    for hasdata in (
        line for line in open('ing.txt')
            if isdata(line)
    )
) )
