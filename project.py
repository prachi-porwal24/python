#!/usr/bin/python3

import os
option='''
1 SHOW IMAGES
2 LAUNCH CONTAINER
3 SHOW CONATINER
4 GET INTO THE CONTAINER
5 DELETE THE CONATINER
'''
print(option)
choice=int(input())

if choice == 1:
 print("HERE THE IMAGES ARE:") 
 os.system('docker images ')

elif choice == 2: 
 image=input("enter the image to be pull:")
 os.system('docker pull ' +image)
 cont=input("enter the container name:")
 os.system('docker run -it --name ' +cont+" "+image)

elif choice == 3:
 options='''
 1 ALL THE CONATINER
 2 STOPPED CONATINER
 3 RUNNING CONTAINER
 '''
 print(options)
 choices=int(input())
 #print(choices)
 #print(type(choices))
 if choices == 1:
  print("ALL CONATINER ARE")
  os.system('docker ps -a')
 elif choice == 2:
  print("STOPPED CONATINER ARE :")
  os.system('docker ps -a | grep -w Exited ')
 elif choice == 3:
  print("RUNNING CONATINER ARE:")
  os.system('docker ps ')

elif choice == 4:
 print("conatiner are")
 os.system('docker ps -a ')
 cont=input("enter the conatiner you want to start:")
 os.system('docker start ' +cont)
 os.system('docker attach ' +cont)
elif choice == 5:
 option='''
 1 TO DELETE ONLY ONE CONATINER
 2 TO DELETE ALL CONATINER
 '''
 print(option)
 choice=int(input())
 if choice == 1:
  cont=input("enter the conatiner name:")
  os.system('docker stop ' +cont)
  os.system(' docker rm ' +cont)
 elif choice == 2:
  print("deleting all the conatiner")
  os.system('docker stop $(docker ps) ')
  os.system(' docker rm $(docker ps -a) ')  
else:
 print("invaliid choice")
