timeout = 1000*60*60
session = 0

def encrypt(something, key):
    return 0

def auth(user, addr):
    f = open("{}.txt".format(user))
    passwd = f.read()
    f.close()

    secret = hash(passwd)
    expiration = time + timeout
    session += 1

    session = encrypt(session, secret)
    ticket = encrypt((user, addr, expiration, session), secret)
    send(session, ticket)
