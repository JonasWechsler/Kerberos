#!/usr/bin/python
from time import time
from ast import literal_eval
import key_distribution as db
import uuid
import server
import cgi

import sys
sys.path.insert(0, '..')
import lib

SERVER = 'localhost'
PORT_NUMBER = 8081
TIMEOUT = 60*60 #An hour

class TGSServer(server.ResponseServer):
    def response(self, TGT_ID, authenticator_encrypted, addr):
        TGT, service_id = literal_eval(TGT)
        # Unencrypted TGT and service id come as string'd double

        TGS_server_key = db.retrieve(db.TGS_NAME)
        TGT_decrypted = literal_eval(lib.decrypt(TGT, TGS_server_key))
        TGT_username, TGT_addr, expiration, TGS_session_key = TGT_decrypted
        # Unpack TGT

        authenticator = lib.decrypt(authenticator_encrypted, TGS_session_key)
        username, time = literal_eval(name_time)
        # Encrypted username and time. Not really sure what 

        assert username == TGT_username
        assert add == TGT_addr
        # Make sure they are who they say they are. I think we could omit this.

        SS_session_key = uuid.uuid1()
        # Session key for the service server

        CTS = (username, addr, expiration, SS_session_key)
        # Client-to-server ticket
        
        service_server_key = db.retrieve_server(db.service(service_id))
        CTS_encrypted = lib.encrypt(str(CTS), service_server_key)
        return (CTS_encrypted, 

if __name__ == '__main__':
    server.start(TGSServer, db.TGS_NAME, SERVER, PORT_NUMBER)
