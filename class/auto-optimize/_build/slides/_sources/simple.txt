simple.py
----------------

.. code-block:: python

     from hyperopt import fmin, tpe, hp
     print fmin(
         fn=lambda x: x ** 2,
         space=hp.uniform('x', -10, 10),
         algo=tpe.suggest,
         max_evals=100)

::

     {'x': 0.028499577187215047}

.. note::

   eval=1	{'x': 3.9293837119572324}
