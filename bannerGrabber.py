import socket

""" 

s = socket.socket()

ip = input('please enter the ip: ')

port = str(input('please enter the port: '))

s.connect((ip, int(port)))

print(s.recv(1024)) #limit receive (bytes)

"""
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print((s.recv(1024)).decode('ascii'))

def main():
    ip = input('please enter the ip: ')
    port = str(input('please enter the port: '))
    banner(ip, port)

main()

# IP IS ROUTER IP, PORT CAN BE FOUND WITH NMAP