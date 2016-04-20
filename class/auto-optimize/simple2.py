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
