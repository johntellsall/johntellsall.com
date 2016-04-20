"""
guessa.py -- word guessing game
Run with "python guessa.py"
"""

answer = 'beer'
while 'forever':
    guess = raw_input("Guess? >")
    if guess == answer:
        print "you win!"
        break
    else:
        print "nope"
