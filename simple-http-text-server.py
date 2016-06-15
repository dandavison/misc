from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
class HTTPRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.vcf': 'text/plain',
    })
if __name__ == '__main__':
    BaseHTTPServer.test(HTTPRequestHandler, BaseHTTPServer.HTTPServer)
