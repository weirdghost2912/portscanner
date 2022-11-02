import socket
import ipaddress


def checkip():
    try:
        ip_obj = ipaddress.ip_address(target)
    except:
        print("invalid ip")
        exit()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

target = input("Enter Host IP to scan::")
checkip()
ports = int(input("Enter Number of ports to scan::"))

print("Starting scan on :", target)
def ps(port):
    try:
        s.connect((target, port))
        return True
    except:
        return False

for port in range(0, ports):
    if ps(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')






