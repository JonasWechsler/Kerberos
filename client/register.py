import client
import sys
import getpass

if __name__ == '__main__':
    sys.stdout.write('Username: ')
    user = raw_input()
    passwd = getpass.getpass()
    client = client.KerberosClient(user, passwd)
    client.register()
