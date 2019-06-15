import socket
recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

choice=raw_input("enter your choice-->1)two way 1) one way")

if choice == "1":
  while 4>3:
   msg=raw_input("enter your message")
   s.sendto(msg,(recv_ip,recv_port))
   print(s.recvfrom(10))

if choice == "2":
  while 4>3:
   msg=raw_input("enter your message")
   s.sendto(msg,(recv_ip,recv_port))

