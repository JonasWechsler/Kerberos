#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from time import time

PORT_NUMBER = 8080
TIMEOUT = 60*60 #An hour

#This class will handles any incoming request from
#the browser 
class AuthenticationServer(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        user = self.path[1:]
        print("Authenticating {}".format(user))

        f = open("{}.txt".format(user))
        passwd = f.read()
        f.close()

        f = open("session")
        session_idx = int(f.read()) + 1
        print("Session index {}".format(session_idx))
        f.write(session_idx)
        f.close()

        secret = hash(passwd) #TODO better hash
        expiration = time() + TIMEOUT
        session = encrypt(session, secret)
	ticket = encrypt_tuple((user, addr, expiration, session), lambda val,
		key: encrypt(val, key))

        self.wfile.write("{}\n{}".format(session, ticket))
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), AuthenticationServer)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
