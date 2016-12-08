import os
from base64 import b64encode

FOLDER = "database"
AS_NAME = "AS"
TGS_NAME = "TGS"
SS_NAME = "SS"

def save(ID, value):
    f = open("{}/{}.data".format(FOLDER, ID), 'w+')
    print("saving {}:{}".format(ID, value))
    f.write(str(value))
    f.close()

def retrieve(ID):
    f = open("{}/{}.data".format(FOLDER, ID))
    data = f.read()
    f.close()
    return data

def configure_server(ID):
    random_bytes = os.urandom(128)
    key = b64encode(random_bytes).decode('utf-8')
    save(ID, key)

def one_way_hash(word):
    #TODO do not do this
    return hash(word)

def configure_user(ID, passwd):
    key = one_way_hash(passwd)
    ID = "user_{}".format(ID)
    save(ID, key)
    return "Registerd {}".format(ID)

def retrieve_user(ID):
    return str(retrieve("user_".format(ID)))

def retrieve_server(ID):
    return str(retrieve(ID))
