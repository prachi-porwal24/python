import socket
recv_ip='127.0.0.1'
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,recv_port))

choice = raw_input("enter your choice: (1) two way (2) one way")

if choice == "1":
  while 4 > 2:
       data=s.recvfrom(100)
       if data[0] == "Y":
          break
       print("message from sender",data[0])
       print("sender ip,sender port-->",data[1])
       s.sendto("ok got it",data[1])


elif choice == "2":
  while 4 > 2:
       data=s.recvfrom(100)
       print("message from sender",data[0])
       print("sender ip,sender port-->",data[1])

else:
      print("invalid choice")
