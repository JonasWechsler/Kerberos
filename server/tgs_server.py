#!/usr/bin/python
from time import time
import key_distribution as db
import uuid
import server
import cgi

PORT_NUMBER = 8081
TIMEOUT = 60*60 #An hour

#This class will handles any incoming request from
#the browser 
class TGSServer(server.ResponseServer):
    def response(TGT, ID, addr):
        secret = db.retrieve_user(username)
        TGS_session_key = uuid.uuid1()
        TGS_encrypted = encrypt(secret, TGS_session_key)

        expiration = time() + TIMEOUT
        TGT = (username, addr, expiration, TGS_session_key)
        TGS_server_key = db.retrieve_server(db.TGS_NAME)
        TGT_encrypted = encrypt_tuple(TGT, lambda v: encrypt(v, TGS_server_key))
        return (TGS_encrypted, TGT_encrypted)


if __name__ == '__main__':
    server.start(AuthenticationServer, db.AS_NAME, 'localhost', 8080)
