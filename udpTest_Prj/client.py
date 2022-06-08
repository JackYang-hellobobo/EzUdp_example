# 1 导包socket
import socket
#获取本机通讯ip地址
hostip = socket.gethostbyname(socket.gethostname())
# 2创建socket对象
# 参数一 指定用ipv4版本，参数2 指定用udp协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3确定要发送的目标ip地址 和 端口  及注意ip是字符串  端口是数字
dest_addr = (hostip, 11000)
# 4确定要发送的内容
print("请输入")
txt = input()
text = txt.encode('utf-8')
# 5用socket对象发送
# 参数1是内容 参数2是地址和端口
udp_socket.sendto(text, dest_addr)
# 6关闭socket对象
udp_socket.close()

