simple2.py
----------------

.. code-block:: python

     from hyperopt import fmin, tpe, hp
     def objective(args):
         x = args
         print x
         return x**2
     print fmin(
         fn=objective,
         space=hp.uniform('x', -10, 10),
         algo=tpe.suggest,
         max_evals=3)

::

     3.92938371196
     -7.87870188091
     0.134520229991
     {'x': 0.13452022999139857}
