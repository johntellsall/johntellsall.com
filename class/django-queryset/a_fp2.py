#!/usr/bin/env python

'''
code isn't executed until needed -- crash later vs earlier
'''

def proc_list(lines):
    for line in lines:
        blam

a = None
try:
    a = proc_list( [1,2] )
except Exception, exc:
    print exc
print 'proc:', a


def proc_iter(lines):
    for line in lines:
        yield blam

try:
    b = proc_iter( [1,2] )
except Exception, exc:
    print exc

print 'iter:', b

try:
    print list(b)
except Exception, exc:
    print exc

