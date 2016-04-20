http://fastml.com/optimizing-hyperparams-with-hyperopt/

https://github.com/hyperopt/hyperopt/wiki/FMin


<!-- f(x)= c*x**3 + a*x**2 + b*x + y0 -->
<!-- fit f(x) 'optimize.dat' via a,b,c,y0 -->
<!-- f(x)= a*x**2 + b*x + y0 -->
<!-- fit f(x) 'optimize.dat' via a,b,y0 -->
f(x)= a*x + y0
fit f(x) 'optimize.dat' via a,y0


plot "optimize.dat" with points lt rgb "#ff0000" title "Points", \
f(x) with lines lt rgb "#ff00ff" title "Approximation"


https://google-developers.appspot.com/chart/interactive/docs/quick_start

interactive testing!
https://code.google.com/apis/ajax/playground/?type=visualization#bar_chart


# XXXX: no
pip install gviz_data_table


"gviz_api" examples
http://google-visualization.appspot.com/python/


wget http://google-visualization-python.googlecode.com/files/gviz_api_py-1.8.2.tar.gz
pip install ./orig/gviz_api_py-1.8.2.tar.gz 

