from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    print 'remember to pick up milk'
    return '<h3>beer is good food</h3>'


port = 8000
httpd = make_server('', port, simple_app)
print "Serving on port {}...".format(port)
httpd.serve_forever()
