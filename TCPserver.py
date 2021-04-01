#!/usr/local/opt/python@3.9/bin/python3.9
import socket

# create server socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket familiy: AF_INET means we're using ipv4
# socket type:  SOCK_STREAM means we're using connection based protocol => TCP (not UDP)

# get host name
host = socket.gethostbyname('localhost')   # host = '127.0.0.1'
print(host)
# specify port
port = 444

# bind the host and port to the server socket object
serversocket.bind((host, port))

# set up a tcp listener (to listen from the client)
# set parameter how many connection we can listen to at a time
serversocket.listen(3)

while True:
    # establish the connection

    # create objects
    clientsocket, address = serversocket.accept() # method: accept => allow TCP connection, accept info

    print("Received connection from %s " % str(address))

    message = 'hello! Thank you for connecting to the server' + '\r\n'

    # send message to client
    clientsocket.send(message.encode('ascii')) # method: send => send info

    # close socket
    clientsocket.close()
# --------------------------------------------------------------------------------------------

