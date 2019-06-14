#ques2= write a code that will take user input from and search on google and store top10 url in list
#!usr/bin/python3
import time
from googlesearch import search
web=input("enter your search:")


url=[]
for i in search(web,stop=10):
	print(i)
	time.sleep(1)
	url.append(i)
print(url)
