#!/usr/local/opt/python@3.9/bin/python3.9
import nmap

scanner = nmap.PortScanner()

print('welcome this is a simple nmap automation tool')
print('<---------------------------------------------')

# GET ROUTER IP HERE
ip_addr = input('Please enter the ip addres you want to scan: ')
print("The IP you entered is: ", ip_addr) 

#sanitize
type(ip_addr)


resp = input("""\nplease enter the type of scan you want to run
                1) SYN ACK scan
                2) UDP scan
                3) comprehensive scan\n""")

print('you have selected option: ', resp)

if resp=='1': #TCP
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('<----------\n')
    print("Ip status: ", scanner[ip_addr].state())
    print('<----------\n')
    print(scanner[ip_addr].all_protocols())
    print('<----------\n')
    # important, all ports that is reachable
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp=='2': #UDP
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU') #sU
    print(scanner.scaninfo())
    print('<----------\n')
    print("Ip status: ", scanner[ip_addr].state())
    print('<----------\n')
    print(scanner[ip_addr].all_protocols())
    print('<----------\n')
    # important, all ports that is reachable
    print("Open ports: ", scanner[ip_addr]['udp'].keys()) # udp
    
elif resp=='3': #UDP
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O') 
    # v erbose, sV enumeration, sC default script, A ggresive scan, O perating system detection
    print(scanner.scaninfo())
    print('<----------\n')
    print("Ip status: ", scanner[ip_addr].state())
    print('<----------\n')
    print(scanner[ip_addr].all_protocols())
    print('<----------\n')
    # important, all ports that is reachable
    print("Open ports: ", scanner[ip_addr]['tcp'].keys()) # tcp

else:
    print("please enter a valid option")
    
    