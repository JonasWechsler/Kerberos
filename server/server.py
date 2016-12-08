from BaseHTTPServer import BaseHTTPRequestHandler
import key_distribution as db
import urlparse


class ResponseServer(BaseHTTPRequestHandler):
    def response(A, B, addr):
        raise NotImplementedError
        return

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qsl(parsed_path.query) + [None]
        A, B = query[0], query[1]
        
        client_address = self.client_address
        message = '\r\n'.join(response(A, B, client_address))
        
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
