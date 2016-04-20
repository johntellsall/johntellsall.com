
.. Python 101 slides file, created by
   hieroglyph-quickstart on Sun Sep 21 12:53:26 2014.


Python 101
==========

Contents:

.. toctree::
   :maxdepth: 2



why are you here?
investment
	will you spend $10 to save 10 hours?
    will you spend 5 hours to save 50 hours?
    - answer SO questions
    - volunteer, write blog posts
why programming
why Python
	- LA companies can't hire fast enough
    - domination: math, science, visual effects, some games
Python versions
	- whatever

NOTES
what's the result?

HELLO WORLD
- print => get output
- "hello" => shell prints the last value

(maybe)
name='beer'
for i in range(3): print 'howdy',name,

AWESOME
- number, loop, math
print "beer" to fill the screen

feature: print num in addition to word

WORD GUESS
- raw_input(), loop, string
set answer word
forever:
	- ask guess
    equal?
    	- "you win!", exit
    - "no luck"


HANGMAN
- loop, string in string
set answer word
ask letter
add to chosen
found:
	"good guess!", change state
	win? "yay", exit
else
	"no luck"

feature: no guesses left? => "better luck next time", exit
feature: at start, ask player's name
feature: read answer from disk
feature: handle upper/lowercase
feature: win => append date + name to highscores file
feature: show highscores file at start
feature: exit if to many guesses
feature: "quit" => quit

PYTHON SHELL
indentation
keyboard commands
"some things are objects, with extra functions"
dir()
help()


PROJECTS
tic tac toe
read 9 words from file
	- print in 3x3 grid
    - random "


help(1) works!; not useful
- skip anything with an underscore; "q" => quit

name='beer'
for i in range(3): print 'howdy',name,


PROGRAMMING CONCEPTS
- variable, type
- loops: while ("forever until"), for ("counting")
- conditional: if, else, (elsif)
- functions
