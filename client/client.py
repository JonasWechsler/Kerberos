import requests
import sys
sys.path.insert(0, '..')
import lib
import urllib
import getpass

URL_AS = 'http://localhost:8080/'
URL_RGB = 'http://localhost:8081/'
URL_SS = 'http://localhost:8082/'

def register(user, passwd):
    return requests.post(URL_AS, data={'username':user, 'password':passwd})

def authenticate(user, passwd):
    args = {'username':user, '_':'_'}
    #Two args just for consistency
    encoded = urllib.urlencode(args)
    response = requests.get(URL_AS + '?' + encoded)

    TGS_key_encoded, TGT = response.content.split()

    secret = lib.one_way_hash(passwd)
    TGS_key = lib.decrypt(TGS_key_encoded, secret)
    print "TGS_key: {}".format(TGS_key_encoded)
    print "TGS_val: {}".format(TGS_key)
    print "TGT: {}".format(TGT)

if __name__ == '__main__':
    sys.stdout.write('Username: ')
    user = raw_input()
    passwd = getpass.getpass()
    authenticate(user, passwd)
