#!/usr/bin/env python

class Upcase(list):
    def __init__(self, inpath):
        super(Upcase,self).__init__(
            open(inpath).readlines()
            )
    def writelines(self, outpath):
        with open(outpath, 'w') as outf:
            for line in self:
                outf.write( line.upper() )

Upcase('ing.txt').writelines('/dev/stdout')
