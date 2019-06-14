import datetime
data=input("enter your name--->")
t = datetime.datetime.now()
if ( t.hour>=6 and t.hour<12  ):
  print("good morning:"+data)
if ( t.hour>=12 and t.hour<=18 ):
  print("good noon:"+data)
if ( t.hour>=19 and t.hour<=5 ):
  print("good night:"+data)


