#!/usr/bin/env python

def upcase(args):
    for arg in args:
        yield arg.upper()

def write(title, args, outpath):
    with open(outpath, 'w') as outf:
        outf.write( title + '\n' )
        for arg in args:
            outf.write( arg )
        outf.write( '\n' )

write( 'FP Lines', 
       upcase( open('ing.txt') ),
       '/dev/stdout',
   )

def lines2words(lines):
    for line in lines:
        for word in line.split():
            yield word

def addcr(arg):
    return arg + '\n'

lines = open('ing.txt')
caplines = upcase( lines )
capwords = lines2words( caplines )
words_cr = ( addcr(word) for word in capwords )
write( 'FP Capwords #1',
       words_cr,
       '/dev/stdout',
   )

write( 'FP Capwords #2',
       map(addcr, lines2words( upcase( open('ing.txt') ) ) ),
       '/dev/stdout',
   )


# print list(
#     map(upcase, open('ing.txt'))
#     )

from itertools import chain
write( 'FP Capwords w/ itertools',
       map(addcr, 
           chain(
               map(
                   lambda line: line.split(),
                   open('ing.txt')
               ),
           ),
       ),
       '/dev/stdout',
   )
