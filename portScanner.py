import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5) # seconds

host = '137.74.187.101' #hackthissite.org PORT 443 is open
port = str(input('input the port you want to scan: '))


def portScanner(host, port):
    if s.connect_ex((host, int(port))): #sends err msg
        print('the port is closed')
    else:   # doesnt send err msg
        print('the port is open')

portScanner(host, port)