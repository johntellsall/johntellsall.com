import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in("johnlmitchell", "jfv445yp4m")

trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace2 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace1, trace2])
