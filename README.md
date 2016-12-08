# Kerberos
![The Kerberos Protocol](https://web.mit.edu/kerberos/images/dog-ring.jpg)

Kerberos is an authentication protocol that allows the user and a server to mutually prove their identity to each other securely. This is done by separating the server into a series of independent server nodes and a trusted logon server. Notable properties of a Kerberos network include:

- Widespread use of symmetric-key cryptography
- Reliance on a trusted third party logon server to verify service nodes
- Service nodes never interact directly with the logon server's central database
- Only requires a transmission of a password once (which I think could be made more secure via Diffie-Hellman key exchange)

### Running the code

You can test the code by running
``` sh
cd test
python test.py
```

You can run all the servers at once by running
``` sh
cd server
python authentication_server.py &
python tgs_server.py &
python service_server_basic.py &
python service_server_bad.py &
python service_server_talkative.py
```

And then in a separate window running
``` sh
cd client
python register.py
```

To make an account and

``` sh
python client.py
```

to run the client. There are three service nodes right now. _Basic_ will start successfully and print out some ASCII art after successfully receiving a message. _Bad_ will start normally but return an incorrect timestamp, exposing itself as a bad server. _Talk_ will loop infinitely repeating what you say back to you, to demonstrate continuous Client-Server interaction.

### Overview
My implementation of the Kerberos protocol involves two log-on servers and a third independent service server. In short, the steps for verification are:

The user sends their username / password pairing once to register themself so the server can hash it and store it under the user's username

##### Authentication (Interaction with the Authentication Server)

- The user sends their username and the server looks up their hashed password
- A: The server sends back a session key (s) hashed by the hashed password
- B: The server sends back a TGT (Ticket-Granting-Ticket), consisting of the user's name, address, expiration date, and session key (s), all hashed with the TGS' (Ticket-Granting-Server) private key

##### Authorization (Interaction with the Ticket Granting Server)

- C: The user sends message B and a service ID
- D: The user sends their ID and timestamp encrypted by their sessionkey S
The server decrypts message C and D
- E: The server sends back a CTS (Client-To-Server ticket) consisting of the user's name, address, expiration date, and Service session key (t) encrypted by the service's private key
- F: The server sends back the Service session key (t) encrypted with their sessionkey S

##### Service Request (Interaction with the Service Node)

- G: The user ends message E
- H: The user sends an authenticator with their name and timestamp encrypted with their Service session key (t)
The server decrypts the ticket E with their secret key and then uses the session key to decrypt H
- I: The server responds with their timestamp encrypted using the Service session key (t)

At this point, if everything goes with issue, the server and client can both be trusted and can communicate via some symmetric encryption like their session key.

### Things I would have done differently

- Right now, I don't have a real database and I just write to files without locking anything. Of course, if I were making a production webserver, I would use a real database service
- Many of the errors that are thrown aren't helpful at all right now, so I would have put in more try/catches to give the user helpful errors
- The TGS and AS don't need to be separate, I just did it that way so I could have a universal "server" class.

### Other details

- I use AES as a symmetric-key encryption method
- I use the obsolete md5 as a one-way hash, because it produces hashes small enough to be used as a key for AES. This is probably priority #1 for issues in the code base.
- Although I wrote a blockchain for encrypting tuples, I ended up just casting the tuples to a string, encrypting that, and then parsing it back to a tuple after decryption, which I think is OK for now because the user never provides the server with text that goes into the tuples.

### Sources

My primary resources were [Wikipedia](https://en.wikipedia.org/wiki/Kerberos_(protocol)), [this blog post](http://www.roguelynn.com/words/explain-like-im-5-kerberos/), and [the MIT page on Kerberos](https://web.mit.edu/kerberos/).

