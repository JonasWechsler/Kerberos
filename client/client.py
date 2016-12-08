def register(user, passwd):
    hashpass = hash(passwd)
    #TODO one-way hash
    f = open("{}.txt".format(user), "w")
    f.write(hashpass)
    f.close()
    #send(user, passwd)

def auth(encr_session, encr_ticket):
    f = open("{}.txt".format(user))
    passwd = f.read()
    f.close()
    secret = hash(passwd)
    session = decrypt(encr_session, secret)
    ticket = decrypt(encr_ticket, secret)

def 
