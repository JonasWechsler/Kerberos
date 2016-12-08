from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class ResponseServer(BaseHTTPRequestHandler):
    def __init__(self, private_key, *args):
        self.private_key = private_key
        BaseHTTPRequestHandler.__init__(self, *args)

    def response(self, A, B, addr):
        raise NotImplementedError
        return

    def resolve(self):
        return 'Please direct queries to /client'

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qsl(parsed_path.query)
        B = query[1][1] if len(query) > 1 else None
        A = query[0][1] if len(query) > 0 else None
        host, port = self.client_address

        if parsed_path.path == '/client':
            message = '\r\n'.join(self.response(A, B, host))
        else:
            message = self.resolve(A, B, host)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(message)
        
        return

import key_distribution as db

def start(response_server, name, url, port):
    from BaseHTTPServer import HTTPServer
    db.configure_server(name)
    private = db.retrieve_server(name)
    def handler(*args):
        response_server(private, *args)
    server = HTTPServer((url, port), handler)
    print "started server on {}:{}".format(url, port)
    server.serve_forever()
