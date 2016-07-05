
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
----------------------------------------------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing 
   * Caching
   * Parallelization

.. rst-class:: build

   - Buzzwordy!

   - Chicks dig it!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


FP vs Procedural programming
----------------------------------------------------------------

**procedural: list of instructions**

input, output, can modify inputs

.. code-block:: python

    def upfile(inpath, outpath):
        with open(outpath, 'w') as outf:
            for line in open(inpath):
                outf.write( line.upper() )
    
    upfile('ing.txt', '/dev/stdout')
    
.. rst-class:: build

   * how can you test this?

   * run in parallel?

.. note::

  [Many] Languages are procedural: programs are lists of instructions
  that tell the computer what to do with the program’s input.


FP vs Object Orientation
----------------------------------------------------------------

procedural: list of instructions

**object oriented: Object has state and specific functions to
query/modify state.  Easy to specialize by subclassing.**

.. code-block:: python

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

.. note::

   Object-oriented programs manipulate collections of objects. Objects
   have internal state and support methods that query or modify this
   internal state in some way. Smalltalk and Java are object-oriented
   languages. C++ and Python are languages that support
   object-oriented programming, but don’t force the use of
   object-oriented features. ["Object obsessive"]

    
Functional Programming
----------------------------------------------------------------

procedural: list of instructions

object oriented: object has state and specific functions to
query/modify state.  Easy to specialize by subclassing

**functional: functions operate on streams of objects**

.. note:: preferably without internal state

FP: list of functions
----------------------------------------------------------------

>>> print '\n'.join( (
    amount(hasdata)
    for hasdata in (
        line for line in open('ing.txt')
            if isdata(line)
    )
) )

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
    
    cursor.execute("""select name from ingridient""")
    
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
    


.. note::
   Generally you'll mix these styles. IE: function that returns
   a stream of objects.
   ****************************************************************


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


Django QuerySets
================================================================

QuerySets are Django's way of getting and updating data

.. note:: models.py

          >>> from django.db import models
          class Meeting(models.Model):
          name = models.CharField(max_length=100)
          meet_date = models.DateTimeField()

QuerySet review
----------------------------------------------------------------
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
----------------------------------------------------------------

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
----------------------------------------------------------------
*How can you tell if a list is empty or not?*

>>> bool([])
False
>>> bool(['beer'])
True

.. note::
   Lists are *eager* -- always know everything

Empty Iterator
----------------------------------------------------------------
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
----------------------------------------------------------------

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
----------------------------------------------------------------

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
----------------------------------------------------------------

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
----------------------------------------------------------------


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
----------------

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

http://blog.etianen.com/blog/2013/06/08/django-querysets/


