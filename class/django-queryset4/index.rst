.. Django QuerySets and Functional Programming #2 slides file, created by
   hieroglyph-quickstart on Sat Jul 19 13:59:19 2014.


Functional Programming and Django QuerySets 7/2016
================================================

LA Django Meetup

July 5th, 2016

INBOX
=====

- add TBT

- add "there will be code"

- queryset.exists() https://docs.djangoproject.com/en/1.9/ref/models/querysets/#exists

In [26]: p=SourceLine.objects.filter(project='redis')

In [27]: str(p.query)
Out[27]: 'SELECT "app_sourceline"."id", "app_sourceline"."project", "app_sourceline"."name", "app_sourceline"."path", "app_sourceline"."line_number", "app_sourceline"."kind", "app_sourceline"."length" FROM "app_sourceline" WHERE "app_sourceline"."project" = redis-2.8.4'

In [30]: p.exists()
Out[30]: True
from django.db import connection
In [31]: connection.queries[-1]
Out[31]: u'QUERY = u\'SELECT (1) AS "a" FROM "app_sourceline" WHERE "app_sourceline"."project" = %s LIMIT 1\' - PARAMS = (u\'redis-2.8.4\',)'


- "What is Functional Programming"

Functions are first class (objects). That is, everything you can do
with “data” can be done with functions themselves (such as
passing a function to another function).
• There is a focus on list processing (for example, it is the source
of the name Lisp). Lists are often used with recursion on sublists
as a substitute for loops.
• “Pure” functional languages eschew side effects. This excludes
the almost ubiquitous pattern in imperative languages of assign‐
ing first one, then another value to the same variable to track
the program state.
• Functional programming either discourages or outright disal‐
lows statements, and instead works with the evaluation of
expressions (in other words, functions plus arguments). In the
pure case, one program is one expression (plus supporting defi‐
nitions).
• Functional programming worries about what is to be computed
rather than how it is to be computed.
• Much functional programming utilizes “higher order” functions
(in other words, functions that operate on functions that oper‐
ate on functions).

- (Esther) python3: xrange/range ; map-filter (imap-ifilter) / map-filter

- "tools that use iterators are more memory efficient (and often faster) than their list based counterparts." https://docs.python.org/3.0/library/itertools.html

- link twitter to website

- short functional library and related FP talk - https://github.com/kachayev/fn.py http://kachayev.github.io/talks/uapycon2012/index.html#/27

- tons of "awesome" links, including to FP in JS https://github.com/xgrommx/awesome-functional-programming

- practical examples, more details https://newcircle.com/bookshelf/python_fundamentals_tutorial/functional_programming

- good intro https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

- Toolz libraries https://github.com/pytoolz/toolz

- book https://www.packtpub.com/application-development/functional-python-programming

- O'Reilly book http://www.oreilly.com/programming/free/functional-programming-python.csp

@johntellsall
=============

talks:
    **Practical Python Testing**

upcoming:
    **Container Deep Dive**

later:
    Networking
    QA-DevOps

.. note::

   - Senior dev/server guy; DevOps
   - 20 years experience with Python
   - john@johntellsall.com

   - first PyCon I went to had 40 people!



Contents
========

iterator/generator = "stream"

Functional Programming: programming with composition

QuerySet is a stream

.. note::

    <https://en.wikipedia.org/wiki/Function_composition_%28computer_science%29>`

   combine simple functions to build more complicated ones


.
--------------

.. figure:: _static/large_BaxterCutawayFF3.jpg
   :class: fill




Iterators
=========


Iterator review
-----------------


An iterator is a *stream* of data |---| sort of a restricted, very
efficient list.

>>> list([1,2])
[1, 2]

>>> iter([1,2])
<listiterator object at 0x7f429d83c750>


.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

.. note::
   mdash: http://docutils.sourceforge.net/FAQ.html

   iterators have a item and next and that's it
   - Preferred, because they take almost no space


You already use iterators
-------------------------

iterate across a *stream* of strings

>>> f = open('recipe.ini')
>>> for line in f:
    print line

::

     # very tasty
     [Old Fashioned]
     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters

.. note::

   you already use iterators

   Ex: Database iterator


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


List vs Iterator
----------------

===========  =======  ==========
feature      list     iterator
===========  =======  ==========
overall      eager    lazy
memory       high     low
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

Common iterator functions
----------------------------------------------------------------

* .. py:function:: enumerate(iter)
* .. py:function:: sorted(iter)
* .. py:function:: range(stop)
* .. py:function:: dict.iteritems()

very important:

* .. py:function:: filter(func/None, iter)
* .. py:function:: map(func, *iterables)

  and *itertools*, and *fileinput*

INBOX: tradeoff readability vs conciseness


☃
=


Functional Programming
==============================


what?
-----

.. image:: _static/jimmy-2.jpg



Practical Advantages to FP
-------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing
   * Caching
   * Parallelization
   * Buzzwordy!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


programming paradigms
---------------------

*procedural*
	list of instructions

        can modify caller's state

*object oriented*
	object has state and functions to query/modify state

        specialize by subclassing


FP vs Procedural programming
----------------------------------------------------------------

*procedural: list of instructions*

.. code-block:: python

    def upfile(inpath, outpath):
        with open(outpath, 'w') as outf:
            for line in open(inpath):
                outf.write( line.upper() )

    upfile('ing.txt', '/dev/stdout')

.. note::

   * how can you test this?

   * run in parallel?

.. note::

  [Many] Languages are procedural: programs are lists of instructions
  that tell the computer what to do with the program’s input.


FP vs Object Orientation
----------------------------------------------------------------

object oriented: Object has state and specific functions to
query/modify state.  Easy to specialize by subclassing.

.. code-block:: python

    class RWFile(list):
        def __init__(self, inpath):
            super(Upcase, self).__init__(open(path))
        def transform(self, line):
            return line
        def writelines(self, outpath):
            with open(outpath, 'w') as outf:
                for line in self:
                    outf.write( self.transform(line) )

    class UpFile(RWFile):
        def transform(self, line):
            return line.upper()

    UpFile('recipe.ini').writelines('/dev/stdout')

.. note::

   Object-oriented programs manipulate collections of objects. Objects
   have internal state and support methods that query or modify this
   internal state in some way. Smalltalk and Java are object-oriented
   languages. C++ and Python are languages that support
   object-oriented programming, but don’t force the use of
   object-oriented features. ["Object obsessive"]


Functional Programming
----------------------------------------------------------------

procedural
    list of instructions

object oriented
    object has state and functions to query/modify state
    specialize by subclassing

**functional**
    **functions operate on streams of objects**

    **combine simple functions => complicated**

    preferably without internal state


food chain
----------

.. image:: _static/FoodChain.jpg



UpFile example in Functional Programming
----------------------------------------

using a generator expression

.. code-block:: python

   open('out.txt', 'w').writelines(
       line.upper() for line in open('in.txt')
   )

.. note::
   seed, then transforms
   recombine elements, vs specialize


UpFile in FP: map
--------------------------------------------

specialize with named function and *map*

.. code-block:: python

    def upcase(line):
        return line.upper()

    open('out.txt', 'w').writelines(
        map(upcase, open('in.txt'))
    )


map-filter
----------

**map(func, iter)** -- `transform` items using a function

.. code-block:: python

    def square(num):
        return num ** 2

>>> map(square, [1,2,3])
[1, 4, 9]


.. note::

   function applies a passed-in function to
   each item in an iterable object and returns a list containing all the
   function call results.

map-filter
----------

**filter(func, iter)** -- provide items `matching` a function

.. code-block:: python

    def is_odd(num):
        return num % 2

>>> filter(is_odd, [1, 2, 3])
[1, 3]



.. note::

   The filter filters out items based on a test function which is a
   filter and apply functions to pairs of item and running result
   which is reduce.



Functional Programming examples
-------------------------------

Example: Windows INI-file parser; aka ConfigParser

1. stream of lines

2. stream of valid lines (no comments, has key-value)

3. stream of key-value match objects

4. dictionary

5. TBD: dict of dictionaries


.. include:: fp-examples.rst


`itertools <https://docs.python.org/2/library/itertools.html>`_
---------------------------------------------------------------

.. hlist::
   *  **chain()**
   *  compress()
   *  count()
   *  cycle()
   *  dropwhile()
   *  groupby()
   *  **ifilter()**
   *  ifilterfalse()
   *  **imap()**
   *  **islice()**
   *  **izip()**
   *  izip_longest()
   *  repeat()
   *  starmap()
   *  takewhile()
   *  tee()

chain -- only for iterators
-----------------------------------------------------------------

**chain(iter*)** gives elements of each stream in order
Equivalent to **+** for lists.

>>> [1,2] + [3]
[1, 2, 3]

>>> from itertools import *
>>> chain(iter([1,2]), iter([3]))
<itertools.chain object at 0x7f429d848510>
>>> list(_)
[1, 2, 3]


.. note::

   stream of objects with state
   lazy vs eager


islice -- similar to list
-------------------------

**islice(iter, num)** -- return first few items

>>> list([1, 2, 3])[:2]
[1,2]

>>> iter([1, 2, 3])[:2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'listiterator' object has no attribute '__getitem__'

>>> itertools.islice(iter([1, 2, 3]), 2)
<itertools.islice object at 0x7f429d7de9f0>
>>> list(_)
[1, 2]
.. note::

   https://docs.python.org/dev/howto/functional.html








☃
=


Django QuerySets
================================================================

represents a *stream* of rows from the database


.. note:: models.py

          source: http://blog.etianen.com/blog/2013/06/08/django-querysets/

          QuerySets are Django's way of getting and updating data

          >>> from django.db import models
          class Meeting(models.Model):
          name = models.CharField(max_length=100)
          meet_date = models.DateTimeField()


QuerySet review
---------------------------------------------------------------
>>> m = Meeting.objects.get(id=12)
<Meeting: Meeting object>

>>> vars( Meeting.objects.get(id=12) )
{'meet_date': datetime.datetime(2014, 5, 20, 7, 0, tzinfo=<UTC>),
'_state': <django.db.models.base.ModelState object at 0x2bd1050>,
'id': 3, 'name': u'LA Django Monthly Meeting'}

>>> x = Meeting.objects.filter(name__icontains='go')
>>> for a in x: print a.name
LA Django Monthly Meeting


QuerySet and iterators
---------------------------------------------------------------

QuerySets can be shifty

>>> x = Meeting.objects.filter(name='java')
>>> x
[]
>>> type(x)
<class 'django.db.models.query.QuerySet'>


Functional QuerySets
================================================================

How can you tell if a list is empty or not?

    * an iterator?

    * a QuerySet?


Empty List?
===========

.. note::

   *How can you tell if a list is empty or not?*

A: Empty List
------------

>>> bool([])
False
>>> bool(['beer'])
True

.. note::
   Lists are *eager* -- always know everything


Empty Iterator?
===============

.. note::
   *How can you tell if an iterator is empty or not?*


A: Empty Iterator
----------------

>>> x=iter([1,2])
>>> bool(x)
True
>>> x=iter([])
>>> bool(x)
True

.. note::
   Iterators are *lazy* -- don't know what they contain!


How can you tell if a QuerySet is empty or not?
================================================================


QuerySet like Iterator
---------------------------------------------------------------

filter with QuerySet:

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

filter with list:

>>> filter(lambda d: d['id']==1, [{'id':1}, {'id':2}])
[{'id': 1}]

filter with iterator:

>>> list(ifilter(lambda d: d['id']==1, iter([{'id':1}, {'id':2}])))
[{'id': 1}]


Because QuerySet *is* an iterator
---------------------------------------------------------------

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

>>> type(Meeting.objects.filter(id=1))
<class 'django.db.models.query.QuerySet'>


.. note::

   similar to iter: dynamic/lazy; list(qs)

   diff: stream of objs, same class
   qs[:3] <=> islice(it, 3)
   bool(iter) vs qs.empty()

   >>> a=iter([])
   >>> bool(a)
   True

   >>> a=[] ; bool(a)
   False

   qs.count()

   laziness is explicit: prefetch_related

   qs.values(); qs.values_list(); qs.values-list(flat=True)


Can mix/match QS/iterators...
---------------------------------------------------------------

>>> Meeting.objects.all()[0].id
1

>>> islice( Meeting.objects.all(), 1).next().id
1

>>> from itertools import *
>>> islice( Meeting.objects.all(), 1)
<itertools.islice object at 0x2bb9ec0>
>>> list(islice( Meeting.objects.all(), 1))
[<Meeting: Meeting object>]


...but not always
----------------


*How can you tell if a QuerySet is empty or not?*

Use x.exists(), not bool(x) -- `more efficient <https://docs.djangoproject.com/en/dev/ref/models/querysets/>`_

.. note::

   Both iterators and QuerySets are *lazy*

   In functional programming, we have functions which operate on infinite-length streams.

   With QuerySets, it's assumed we have many thousands of results, but we don't want to fetch all of them at once before returning to caller.

   Database (and Django) does a query, then gives us a few items.  Once that batch is done, QuerySet will ask the database for another batch of results.

   This means that for both iterators and query sets, we can do a
   little work, then process a batch, without waiting for the entire
   list of results.


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



References
---------------

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

(best blog title ever)

http://blog.etianen.com/blog/2013/06/08/django-querysets/

.. Django QuerySets and Functional Programming slides file, created by
   hieroglyph-quickstart on Mon May 12 14:08:05 2014.

Django QuerySets and Functional Programming
===================================================

john@johntellsall.com

v2

THEME
================

By using techniques from Functional Programming, we can
make modular, reliable and testable code, faster.

ME
====

   - Senior dev/server guy; Devops
   - 15 years experience with Python
   - first PyCon I went to had 40 people!

.. note::
      Functional Programming <funcprog>
      FP in Python <fp_python>
      querysets
      Patterns and Consequences <pat_conseq>
      summary

.. note::
   stream of objects with state
   lazy vs eager
   Heisenberg
   ****************************************************************


.. note::   figure:: /_static/3-hoodlums-nancy.png
  slide:: Three Programming Paradigms


Why Functional Programming
================================================================

Practical Advantages to Functional Programming
---------------------------------------------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing
   * Caching
   * Parallelization

.. rst-class:: build

   - Buzzwordy!

   - Chicks dig it!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability





.. note:: add "happy girl with beads" image


.. note::

   Data streams from function to function -- no side effects.

   read Andy Kuchling's `Functional Programming HOWTO`_

.. _`Functional Programming HOWTO`: https://docs.python.org/2.7/howto/functional.html

.. note::
   Functional programming decomposes a problem into a set of
   functions. Ideally, functions only take inputs and produce outputs,
   and don’t have any internal state that affects the output produced
   for a given input.

   Eliminating side effects, i.e. changes in state that do not depend
   on the function inputs, can make it much easier to understand and
   predict the behavior of a program

   http://en.wikipedia.org/wiki/Functional_programming


Iterators
---------------

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
---------------

iterate across a *stream* of strings

.. code-block:: python

    f = open('beer.txt')
    for line in f:
        print line

.. note::

   you already use iterators

List very similar to Iterator
---------------------------------------------------------------

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



FP: upcase
---------------------------------------------------------------

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
---------------------------------------------------------------

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



.. note::
   Generally you'll mix these styles. IE: function that returns
   a stream of objects.
   ****************************************************************


Functional Programming in Python
================================================================

Old Primary Functions
---------------------------------------------------------------

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
---------------------------------------------------------------

>>> print open('ing.txt')
# Old Fashioned
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters

Functional Prog for Better Booze!
---------------------------------------------------------------

.. figure:: /_static/Oldfashioned-cocktail.png

   CC PD http://en.wikipedia.org/wiki/File:Oldfashioned-cocktail.png

FP: filter
---------------

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
---------------

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
---------------------------------------------------------------

**filter replacement**

>>> print (line for line in open('ing.txt') if 'whiskey' in line)

**compare with**

*filter(function, iterable)*

.. note::
   high performance, memory efficient generalization of list comprehensions [1] and generators [2].
   http://legacy.python.org/dev/peps/pep-0289/


Preferred: filter replacement
---------------------------------------------------------------

>>> print (line for line in open('ing.txt') if 'whiskey' in line)
<generator object <genexpr> at 0x7f429d7c8eb0>

convert to list so we can see
---------------------------------------------------------------

>>> print list((line for line in open('ing.txt') if 'whiskey' in line)**)
['1.5 oz whiskey\n']

original FP #1
---------------------------------------------------------------
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
---------------------------------------------------------------
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
---------------------------------------------------------------

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
---------------------------------------------------------------

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
---------------------------------------------------------------

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


Django QuerySets
================================================================

QuerySets are Django's way of getting and updating data

.. note:: models.py

          >>> from django.db import models
          class Meeting(models.Model):
          name = models.CharField(max_length=100)
          meet_date = models.DateTimeField()

QuerySet review
---------------------------------------------------------------
>>> m = Meeting.objects.get(id=12)
<Meeting: Meeting object>

>>> Meeting.objects.get(id=12).__dict__
{'meet_date': datetime.datetime(2014, 5, 20, 7, 0, tzinfo=<UTC>),
'_state': <django.db.models.base.ModelState object at 0x2bd1050>,
'id': 3, 'name': u'LA Django Monthly Meeting'}

>>> x = Meeting.objects.filter(name__icontains='go')
>>> for a in x: print a.name
LA Django Monthly Meeting


QuerySet and iterators
---------------------------------------------------------------

>>> x=Meeting.objects.filter(name='java')
>>> x
[]
>>> type(x)
<class 'django.db.models.query.QuerySet'>

Functional QuerySets
================================================================

.. rst-class:: build

   How can you tell if a list is empty or not?

   . an iterator?

   . a QuerySet?

Empty List
---------------------------------------------------------------
*How can you tell if a list is empty or not?*

>>> bool([])
False
>>> bool(['beer'])
True

.. note::
   Lists are *eager* -- always know everything

Empty Iterator
---------------------------------------------------------------
*How can you tell if an iterator is empty or not?*

>>> x=iter([1,2])
>>> bool(x)
True
>>> x=iter([])
>>> bool(x)
True

.. note::
   Iterators are *lazy* -- don't know what they contain!

How can you tell if a QuerySet is empty or not?
================================================================


QuerySet like Iterator
---------------------------------------------------------------

filter with QuerySet:

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

filter with list:

>>> filter(lambda d: d['id']==1, [{'id':1}, {'id':2}])
[{'id': 1}]

filter with iterator:

>>> list(ifilter(lambda d: d['id']==1, iter([{'id':1}, {'id':2}])))
[{'id': 1}]

Because QuerySet *is* an iterator
---------------------------------------------------------------

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

>>> type(Meeting.objects.filter(id=1))
<class 'django.db.models.query.QuerySet'>


.. note::

   similar to iter: dynamic/lazy; list(qs)

   diff: stream of objs, same class
   qs[:3] <=> islice(it, 3)
   bool(iter) vs qs.empty()

   >>> a=iter([])
   >>> bool(a)
   True

   >>> a=[] ; bool(a)
   False

   qs.count()

   laziness is explicit: prefetch_related

   qs.values(); qs.values_list(); qs.values-list(flat=True)

Can mix and match
---------------------------------------------------------------

>>> Meeting.objects.all()[0].id
1

>>> islice( Meeting.objects.all(), 1).next().id
1

>>> from itertools import *
>>> islice( Meeting.objects.all(), 1)
<itertools.islice object at 0x2bb9ec0>
>>> list(islice( Meeting.objects.all(), 1))
[<Meeting: Meeting object>]

But not always
---------------------------------------------------------------


*How can you tell if a QuerySet is empty or not?*

Use x.exists(), not bool(x) -- more efficient

.. note::

   Both iterators and QuerySets are *lazy*

   In functional programming, we have functions which operate on infinite-length streams.

   With QuerySets, it's assumed we have many thousands of results, but we don't want to fetch all of them at once before returning to caller.

   Database (and Django) does a query, then gives us a few items.  Once that batch is done, QuerySet will ask the database for another batch of results.

   This means that for both iterators and query sets, we can do a
   little work, then process a batch, without waiting for the entire
   list of results.


Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   john@johntellsall.com


References
---------------

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

http://blog.etianen.com/blog/2013/06/08/django-querysets/





HISTORICAL
---------

..
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


Database iterator
-------------------

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


FP: Lisp style with generator expressions
---------------------------------------------------------------

XX

*print list of ingredients in a recipe*

.. code-block:: python

    print '\n'.join(
        map(ing_name,
            filter(None,
                   map(parse_ing,
                       open('oldfashioned.ini')
                   )
            )
        ))

FP: Lisp style with map-filter
---------------------------------------------------------------

*print list of ingredients in a recipe*

XX

.. code-block:: python

   print '\n'.join(
       map(ing_name,
       filter(None,
            map(parse_ing,
                open('ing.txt')
            )
        )
   )

imap-ifilter
-----------

>>> import itertools

>>> itertools.imap(square, [1,2])
<itertools.imap at 0x7fc004e6bb50>

>>> list(itertools.imap(square, [1,2]))
[1, 4]


Ex2: print list of ingredients in a recipe
------------------------------------------

**oldfashioned.ini**::

     # very tasty
     [Old Fashioned]
     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters

::

   whiskey
   water
   sugar
   bitters

Ex2: procedural style
---------------------

*print list of ingredients in a recipe*

.. code-block:: python

    ingredients = []
    for line in open('oldfashioned.ini'):
        ing = parse_ing(line)
        if ing:
            ingredients.append(ing.name)
    print '\n'.join(ingredients)

.. note::
    def parse_ing(line):
        return re.match(r'[0-9].+\s(?P<name>\w+)', line)
