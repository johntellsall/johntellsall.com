#!/usr/bin/env python

import time

name = raw_input("What is your name? ")
print "Hi,", name, "!"
print

with open('word.dat') as wordfile:
    word = wordfile.readline()

# letters: list of strings; each unique letter in answer
letters = []
for letter in word:
    if letter >= 'a' and letter <= 'z':
        letters.append( letter )

guesses = []
while True:
    letter = raw_input('What is your guess? ')
    if letter in letters:
        print 'Great guess!'
    else:
        print 'Nope'
    print

