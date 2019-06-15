#!/usr/bin/python3
option='''
press 1 to read a file:
press 2 to copy content of one file into another
press 3 to append
'''
print(option)
choice=int(input())

if choice == 1:
 print("for displaying the content of data")
 f=open('hello.txt','r')
 data=f.read()
 print(data)
 f.close()

elif choice == 2:
 print("for copying the content of one file into another")
 f1=open("hey.txt",'w+')
 f=open("hello.txt",'r')
 data=f.read()
 print(data)
 for i in data:
   f1.write(i)
 f1.close()
 f1=open("hey.txt",'r')
 data1=f1.read()
 print(data1)
 f1.close()

elif choice == 3:
 print("for appending the content of file")
 f=open("hello.txt",'a')
 f.write("pythn")
 f=open("hello.txt",'r')
 print(f.read())
 f.close()
 
else:
 print("invalid choice")

