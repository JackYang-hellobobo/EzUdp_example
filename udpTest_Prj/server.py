
import socket
#获取本机通讯ip地址
hostip = socket.gethostbyname(socket.gethostname())
# 2创建socket对象
# 参数一 指定用ipv4版本，参数2 指定用udp协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3 绑定地址和端口
udp_socket.bind((hostip, 11000))
# 4接收数据 等待
recv_data = udp_socket.recvfrom(1024)
# 5显示一下收到的信息
print('接收的内容：', recv_data[0].decode('utf-8'))
# 6关闭socket对象
udp_socket.close()