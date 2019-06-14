#ques 3
#!usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
value=5
pp=[]
rr=[]
for i in adhoc:
    if(i > 5):
      print(i)
      pp.append(i)
    if(i <= 2):
      print(i)
      rr.append(i)
print("first list is")
print(pp)
print("second list is")
print(rr)
