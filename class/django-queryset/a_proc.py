#!/usr/bin/env python

def uplines(inpath, outpath):
    with open(outpath, 'w') as outf:
        for line in open(inpath):
            upline = line.upper()
            outf.write( upline )

uplines('ing.txt', '/dev/stdout')

def upwords(inpath, outpath):
    with open(outpath, 'w') as outf:
        for line in open(inpath):
            line = line.upper()
            for word in line.split():
                word_cr = word + '\n'
                outf.write( word_cr )

upwords('ing.txt', '/dev/stdout')

