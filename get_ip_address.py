#get ip address by python
import socket
hostname=socket.gethostname()
ip_add=socket.gethostbyname(hostname)
print(f"My ip address is:{ip_add} ")