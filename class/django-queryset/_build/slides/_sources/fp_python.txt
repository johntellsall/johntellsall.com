Functional Programming in Python
================================================================

Old Primary Functions
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

.. py:function:: reduce(function, iterable[, initializer])

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

.. figure:: /_static/bourbon-old-fashioned.jpg

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


Recommended: generator expressions
----------------------------------------------------------------

**filter replacement**

>>> print (line for line in open('ing.txt') if 'whiskey' in line)

**compare with**

*filter(function, iterable)*

.. note::
   high performance, memory efficient generalization of list comprehensions [1] and generators [2].
   http://legacy.python.org/dev/peps/pep-0289/


filter replacement
----------------------------------------------------------------

>>> print (line for line in open('ing.txt') if 'whiskey' in line)
<generator object <genexpr> at 0x7f429d7c8eb0>

filter replacement
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

.. py:function:: chain(*iterables)

.. py:function:: ifilter()	pred, seq	elements of seq where pred(elem) is True	ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
.. py:function:: ifilterfalse()	pred, seq	elements of seq where pred(elem) is False	ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
.. py:function:: islice()	seq, [start,] stop [, step]	elements from seq[start:stop:step]	islice('ABCDEFG', 2, None) --> C D E F G
.. py:function:: imap()	func, p, q, ...	func(p0, q0), func(p1, q1), ...	imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
.. py:function:: starmap()	func, seq	func(*seq[0]), func(*seq[1]), ...	starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
.. py:function:: tee()	it, n	it1, it2 , ... itn splits one iterator into n	 
.. py:function:: takewhile()	pred, seq	seq[0], seq[1], until pred fails	takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
.. py:function:: izip()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip('ABCD', 'xy') --> Ax By
.. py:function:: izip_longest()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-




iter: chain
----------------------------------------------------------------

**chain(streams)** gives elements of each stream in order

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
