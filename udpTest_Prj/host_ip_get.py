import socket
hostip = socket.gethostbyname(socket.gethostname())
print("Local IP Address: "+hostip)