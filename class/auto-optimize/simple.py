from hyperopt import fmin, tpe, hp
print fmin(
    fn=lambda x: x ** 2,
    space=hp.uniform('x', -10, 10),
    algo=tpe.suggest,
    max_evals=1)

# # AUX
# import plotly.plotly as py
# from plotly.graph_objs import *

# xlist = range(-10, 10)
# trace0 = Scatter(
#     x=xlist,
#     y=[x**2 for x in xlist],
#     name='x^2',
#     # line=Line(shape='spline'),
# )
# data = Data([trace0])
# unique_url = py.plot(data, filename = 'simple')
