parse1.py
----------------

.. code-block:: python

     # 1. stream of lines
     import fileinput
     lines = fileinput.input()
     print ''.join( lines )

::

     # very tasty
     [Old Fashioned]
     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters
     
     
parse2.py
----------------

.. code-block:: python

     # 2. stream of valid lines
     import fileinput
     from itertools import *
     def has_comment(line):
         return line.startswith('#')
     def has_keyvalue(line):
         return ':' in line
     lines = ifilterfalse( has_comment, fileinput.input() )
     lines = ifilter( has_keyvalue, lines )
     print ''.join( lines )

::

     1:1.5 oz whiskey
     2:1 tsp water
     3:0.5 tsp sugar
     4:2 dash bitters
     
     
parse3.py
----------------

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
     
parse4.py
----------------

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
     matches = (parse_keyvalue(line) for line in lines)
     keyvalues = ifilter(None, matches)
     confdict = dict(keyvalues)
     print confdict

::

     {'1': '1.5 oz whiskey', '3': '0.5 tsp sugar', '2': '1 tsp water', '4': '2 dash bitters'}
     
