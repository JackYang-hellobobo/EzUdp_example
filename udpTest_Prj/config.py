import socket

#Setting IP and Port
hostip = socket.gethostbyname(socket.gethostname())
ip_port = input()
dest_addr = (hostip,int(ip_port))

#Create A Socket Case
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Set Msn
source_msn=input("Please Enter Msn:")
codemsn = source_msn.encode('utf-8')

#Socket Case Send Msn
udp_socket.sendto(codemsn,dest_addr)

#Close the Socket Case
udp_socket.close()

if __name__=='__main__':
    print("As Script Run")
else:
    print("As Packge Import")


