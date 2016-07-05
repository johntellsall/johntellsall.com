
.. Django QuerySets and Functional Programming #2 slides file, created by
   hieroglyph-quickstart on Sat Jul 19 13:59:19 2014.


Django QuerySets and Functional Programming
===========================================

for Professional Python group at TrueCar

July 22, 2014


ME
====

   - Senior dev/server guy; DevOps
   - 15 years experience with Python
   - john@johntellsall.com

.. note::

   - first PyCon I went to had 40 people!


IDEAS
=====

iterator/generator = "stream"

FP: programming with composition

QuerySet is a stream

.. note::

	- itertools
	- functions

	- no side effects


overview
--------

.. image:: _static/large_BaxterCutawayFF3.jpg


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


File iterator
----------------

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


Very similar
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


Common Iterator Functions
----------------------------------------------------------------

* .. py:function:: enumerate(iter)
* .. py:function:: sorted(iter)
* .. py:function:: range(stop)

very important:

* .. py:function:: filter(func/None, iter)
* .. py:function:: map(func, *iterables)


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

☃
=


Functional Programming
==============================


what?
-----

.. image:: _static/jimmy-2.jpg



food chain
----------

.. image:: _static/FoodChain.jpg



programming styles
------------------

*procedural*

	list of instructions

*object oriented*

	object has state and functions to query/modify state; specialize by subclassing

**functional**

	functions operate on streams of immutable objects

.. note::

   https://docs.python.org/dev/howto/functional.html


Practical Advantages to FP
--------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing 
   * Caching
   * Parallelization
   * Buzzwordy!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


Functional Programming examples
-------------------------------

Example: Windows INI-file parser; aka ConfigParser

1. stream of lines

2. stream of valid lines (no comments, has key-value)

3. stream of key-value match objects

4. dictionary

5. TBD: dict of dictionaries


.. include:: fp-examples.rst


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
----------

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
-----------------

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


Can mix/match QS/iterators...
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


...but not always
--------------


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
----------------

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

(best blog title ever)

http://blog.etianen.com/blog/2013/06/08/django-querysets/
