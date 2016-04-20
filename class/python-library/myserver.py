import BaseHTTPServer, logging, os, SimpleHTTPServer
from CGIHTTPServer import *

LOG = logging.getLogger(__name__)


class MyCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def is_cgi(self):
        if os.path.splitext(self.path)[-1] != '.cgi':
            return False
        self.cgi_info = self.path.rsplit('/',1)
        LOG.debug("cgi_info = {}".format(self.cgi_info))
        return True

def test(
        HandlerClass = MyCGIHTTPRequestHandler,
        ServerClass = BaseHTTPServer.HTTPServer):
    SimpleHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
