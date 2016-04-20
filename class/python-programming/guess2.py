#!/usr/bin/env python

import sys

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
    print '* letters=',letters,'guesses=',guesses
    guess = raw_input('What is your guess? ')
    if guess in guesses:
        print 'You already guessed that!'
        continue
    guesses.append( guess )

    if guess in letters:
        print 'Great guess!'
        letters.remove(guess)
        if not letters:
            print '*'*50
            print 'YOU WIN!'
            print '*'*50
            sys.exit(1)
    else:
        print 'Nope'

    print

