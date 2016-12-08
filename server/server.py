from BaseHTTPServer import BaseHTTPRequestHandler
import key_distribution as db
import urlparse

class ResponseServer(BaseHTTPRequestHandler):
    def response(self, A, B, addr):
        raise NotImplementedError
        return

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qsl(parsed_path.query)
        A, B = query[0][1], query[1][1]
        
        message = '\r\n'.join(self.response(A, B, self.client_address))
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(message)
        
        return

def start(response_server, name, url, port):
    from BaseHTTPServer import HTTPServer
    db.configure_server(name)
    server = HTTPServer((url, port), response_server)
    print "started server on {}:{}".format(url, port)
    server.serve_forever()
