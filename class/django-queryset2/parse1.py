# 1. stream of lines
import fileinput
lines = fileinput.input() 
print ''.join( lines )
