#!/usr/local/opt/python@3.9/bin/python3.9
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname('localhost')   # host = '127.0.0.1'
# /etc/hosts, get host by name, register name before use

port = 444 # match the TCP server port

clientsocket.connect((host,port))

message = clientsocket.recv(1024) # maximum data being transmitted by the tcp (1024 bytes)

# let's decode the ascii
clientsocket.close()

print(message.decode('ascii'))