.. Django QuerySets and Functional Programming #2 slides file, created by
   hieroglyph-quickstart on Sat Jul 19 13:59:19 2014.


Iterators are Awesome
================================================

John Tells All Hack Day

July 15, 2017


ME
====

   - Senior dev/server guy; DevOps
   - 20 years experience with Python
   - @johntellsall.com

.. note::

   - first PyCon I went to had 40 people!


Contents
=====

- iterator basics
- comparison with lists
- important differences
- useful functions in `itertools`


Iterators
----------------

An iterator is a *stream* of data -- sort of a restricted, very
efficient list

>>> list([1,2])
[1, 2]

>>> iter([1,2])
<listiterator object at 0x7f429d83c750>

.. note::

   iterators have a item and next and that's it
   - Preferred, because they take almost no space


File iterator
----------------

iterate across a *stream* of strings

.. code-block:: python

    f = open('beer.txt')
    for line in f:
        print line

.. note::

   you already use iterators

Database iterator
--------------------

iterate with a *stream* of rows

.. code-block:: python

    import os, sqlite3
    conn = sqlite3.connect('recipe')
    cursor = conn.cursor()

    cursor.execute("""select name from ingredient""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

List very similar to Iterator
----------------------------------------------------------------

.. code-block:: python

   for line in open('ing.txt'):
       print line

   for num in iter([2,4,6,8]):
       print num

   for num in [2,4,6,8]:
       print num

   for name in glob.glob('*.txt'):
       print name

Work with a *stream* of objects



What can you do with a iterator?
----------------------------------------------------------------

>>> f = open('ing.txt')
>>> f.next()
'# Old Fashioned\n'
>>> f.next()
'1.5 oz whiskey\n'


What happens at the end?
----------------------------------------------------------------

>>> f = open('/dev/null')
>>> f.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> iter([]).next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration



Lists/Iterators are very similar
----------------------------------------------------------------

.. code-block:: python

   for line in open('ing.txt'):
       print line

   for num in iter([2,4,6,8]):
       print num

   for num in [2,4,6,8]:
       print num

   for name in glob.iglob('*.txt'):
       print name


What can you *not* do with an iterator?
---------------------------------------

**no slicing**

>>> f = open('ing.txt')
>>> f[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'file' object has no attribute '__getitem__'


What can you *not* do with an iterator?
---------------------------------------

**no length**

>>> f = open('ing.txt')
>>> len(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'file' has no len()


You already use common iterator functions
----------------------------------------------------------------

* .. py:function:: enumerate(iter)
* .. py:function:: sorted(iter)
* .. py:function:: range(stop)

very important:

* .. py:function:: filter(func/None, iter)
* .. py:function:: map(func, *iterables)

  and _itertools_


`itertools <https://docs.python.org/2/library/itertools.html>`_
---------

.. hlist::
   *  **chain()**
   *  count()
   *  cycle()
   *  repeat()
   *  **chain()**
   *  compress()
   *  dropwhile()
   *  groupby()
   *  **ifilter()**
   *  ifilterfalse()
   *  **islice()**
   *  imap()
   *  starmap()
   *  tee()
   *  takewhile()
   *  **izip()**
   *  izip_longest()


islice -- similar to list
-------------------------

**islice(iter, num)** -- return first few items

>>> list([1,2,3])[:2]
[1,2]

>>> from itertools import *
>>> iter([1,2,3])[:2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'listiterator' object has no attribute '__getitem__'
>>> islice(iter([1,2,3]), 2)
<itertools.islice object at 0x7f429d7de9f0>
>>> list(_)
[1, 2]


chain -- only for iterators
----------------------------------------------------------------

**chain(iter*)** gives elements of each stream in order
Equivalent to **+** for lists.

>>> [1,2]+[3]
[1, 2, 3]

>>> from itertools import *
>>> chain(iter([1,2]), iter([3]))
<itertools.chain object at 0x7f429d848510>
>>> list(_)
[1, 2, 3]


.. note::

   stream of objects with state
   lazy vs eager
   ****************************************************************


List vs Iterator
----------------

===========  =======  ==========
feature      list     iterator
===========  =======  ==========
overall      eager    lazy
len(x)       yes      no
slice        x[:3]    islice(x, 3)
addition     x + y    chain(x, y)
has items    if x     no
easy debug   yes      no
===========  =======  ==========

.. note::

   List are "eager" -- know everything about them all the time

   Million item list can be rough, because they hold all million
   - have to deal with all items

   Million item iter is no biggie, can proc a few


☃
=







FP: upcase
----------------------------------------------------------------

functional: functions operate on streams of objects

.. code-block:: python

    def upcase(lines):
        for line in lines:
            yield line.upper()

    def writelines(outpath, lines):
        with open(outpath, 'w') as outf:
            for line in lines:
                outf.write( line )

    writelines( '/dev/stdout',
                upcase( open('ing.txt') )
                )

FP: upcase 2
----------------------------------------------------------------

.. code-block:: python

    def upcase(lines):
        # IN: stream of lines; OUT: stream of lines
        for line in lines:
            yield line.upper()

    def writelines(outpath, lines):
        # IN: stream of lines; OUT: nothing
        with open(outpath, 'w') as outf:
            for line in lines:
                outf.write( line )

    # open() is OUT: stream of lines
    writelines( '/dev/stdout',
                upcase( open('ing.txt') )
                )















Iterators
=========




IDEAS
=====

iterator/generator = "stream"

FP: functions operate on streams of immutable objects

QuerySet is a stream

.. note::
   programming with composition


.. rst-class:: questions

Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   john@johntellsall.com





Functional Programming in Python
================================================================

Primary Functions
----------------------------------------------------------------

.. py:function:: filter(function, iterable)

   Construct a **list** from those elements of iterable for which function returns true.

.. py:function:: map(function, iterable, ...)

   Apply function to every item of iterable and return a **list** of the results.

>>> map(None, (1,2))
[1, 2]

.. note:: If additional iterable arguments are passed, function must
   take that many arguments and is applied to the items from
   all iterables in parallel. If one iterable is shorter than
   another it is assumed to be extended with None items. If
   function is None, the identity function is assumed; if there
   are multiple arguments, map() returns a list consisting of
   tuples containing the corresponding items from all iterables
   (a kind of transpose operation). The iterable arguments may
   be a sequence or any iterable object; the result is always a
   list.

.. note:: .. py:function:: reduce(function, iterable[, initializer])

   Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.


.. note:: .. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)


FP: important dataset
----------------------------------------------------------------

>>> print open('ing.txt')
# Old Fashioned
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters

Functional Prog for Better Booze!
----------------------------------------------------------------

.. figure:: /_static/Oldfashioned-cocktail.png

   CC PD http://en.wikipedia.org/wiki/File:Oldfashioned-cocktail.png

FP: filter
----------------

>>> def isdata(line):
    return not line.startswith('#')

>>> print ''.join( filter(isdata, open('ing.txt')) )
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters

.. py:function:: filter(function, iterable)

   Construct a **list** from those elements of iterable for which function returns true.


FP: map, filter
----------------

>>> def amount(line):
    return str(line.split()[:2])
>>> def isdata(line):
    return not line.startswith('#')

>>> print '\n'.join( map(amount, filter(isdata, open('ing.txt'))) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']

.. py:function:: map(function, iterable, ...)

   Apply function to every item of iterable and return a **list** of the results.


Preferred: generator expressions
----------------------------------------------------------------

**filter replacement**

>>> print (line for line in open('ing.txt') if 'whiskey' in line)

**compare with**

*filter(function, iterable)*

.. note::
   high performance, memory efficient generalization of list comprehensions [1] and generators [2].
   http://legacy.python.org/dev/peps/pep-0289/


Preferred: filter replacement
----------------------------------------------------------------

>>> print (line for line in open('ing.txt') if 'whiskey' in line)
<generator object <genexpr> at 0x7f429d7c8eb0>

convert to list so we can see
----------------------------------------------------------------

>>> print list((line for line in open('ing.txt') if 'whiskey' in line)**)
['1.5 oz whiskey\n']

original FP #1
----------------------------------------------------------------
>>> def isdata(line):
    return not line.startswith('#')

>>> def amount(line):
    return str(line.split()[:2])

>>> print '\n'.join( map(amount, filter(isdata, open('ing.txt'))) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']


updated FP #1
----------------------------------------------------------------
>>> def isdata(line):
    return not line.startswith('#')

>>> def amount(line):
    return str(line.split()[:2])

>>> print '\n'.join( (
    amount(hasdata)
    for hasdata in (
        line for line in open('ing.txt')
            if isdata(line)
    )
) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']




Iterator Functions
----------------------------------------------------------------

.. py:function:: xrange(stop) -> counter (xrange object)

.. py:function:: xrange(start, stop[, step]) -> counter

.. py:function:: chain(*iterables) -> each item in order

.. py:function:: ifilter(f, iter) -> substream of iter. Like filter, for iterators.

.. py:function:: islice(iter, num) -> counted items of iter


.. note::
   .. py:function:: imap(func, p, q) -> f(p), f(q), ...

                    .. py:function:: izip()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip('ABCD', 'xy') --> Ax By
                                     .. py:function:: izip_longest()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-



iter: chain
----------------------------------------------------------------

**chain(streams)** gives elements of each stream in order
Equivalent to **+** for lists.

>>> [1,2]+[3]
[1, 2, 3]

>>> from itertools import *
>>> chain(iter([1,2]), iter([3]))
<itertools.chain object at 0x7f429d848510>
>>> list( chain(iter([1,2]), iter([3])) )
[1, 2, 3]


.. note::

   stream of objects with state
   lazy vs eager
   ****************************************************************

iter: islice
----------------------------------------------------------------

**islice(stream, num)** -- get counted elements of stream
Equivalent to slice operator for lists.

>>> list([1,2,3])[:1]
[2]

>>> from itertools import *
>>> iter([1,2,3])[:1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'listiterator' object has no attribute '__getitem__'
>>> islice(iter([1,2,3]), 2)
<itertools.islice object at 0x7f429d7de9f0>
>>> list(islice(iter([1,2,3]), 2))
[1, 2]


