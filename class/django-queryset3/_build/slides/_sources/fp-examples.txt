FP in two step workflow
-----------------------

.. code-block:: python

     # 1. stream of lines
     lines = open('recipe.ini')
     print ''.join( lines )

::

     # very tasty
     [Old Fashioned]
     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters


FP workflow with ifilter
------------------------

.. code-block:: python

     # 2. stream of valid lines
     from itertools import *
     def has_comment(line):
         return line.startswith('#')
     def has_keyvalue(line):
         return ':' in line
     lines = open('recipe.ini')
     lines = ifilterfalse( has_comment, lines )
     lines = ifilter( has_keyvalue, lines )
     print ''.join( lines )

::

     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters


FP with generator expression and ifilter
----------------------------------------

.. code-block:: python

     # 3. stream of key-value match objects
     import fileinput, re
     from itertools import *
     def has_comment(line):
         return line.startswith('#')
     def parse_keyvalue(line):
         m = re.match(r'(\S+):(.+)', line)
         if m:
             return m.groups()
         return None
     matches = (parse_keyvalue(line) for line in fileinput.input())
     keyvalues = ifilter(None, matches)
     print '\n'.join( (str(kv) for kv in keyvalues) )

::

     ('1', '1.5 oz whiskey')
     ('2', '1 tsp water')
     ('3', '0.5 tsp sugar')
     ('4', '2 dash bitters')


FP with map-ifilter, dict output
--------------------------------

.. code-block:: python

     # 4. dictionary
     import fileinput, re
     from itertools import *
     def has_comment(line):
         return line.startswith('#')
     def parse_keyvalue(line):
         m = re.match(r'(\S+):(.+)', line)
         if m:
             return m.groups()
         return None
     lines = ifilterfalse(has_comment, fileinput.input())
     matches = map(parse_keyvalue, lines)
     keyvalues = ifilter(None, matches)
     confdict = dict(keyvalues)
     print confdict

::

     {'1': '1.5 oz whiskey', '3': '0.5 tsp sugar',
      '2': '1 tsp water', '4': '2 dash bitters'}
