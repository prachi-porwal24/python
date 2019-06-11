#!/usr/bin/python3
import webbrowser
import time
import subprocess
option='''
Press 1 to start my vlc media player:
Press 2 to play my favourite song in youtube:
Press 3 to search something on google:
Press 4 to send whatsapp message to my favourite no.:
Press 5 to check current time and date:
Press 6 to reboot my machine:
'''
print(option)

# Taking inputs from users
choice=input()
# conditional state

if choice == '2' :
     # To play favourite song in youtube
     data=input("Type your search:--->  ")
     webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+data)

elif choice == '1' :
     subprocess.getoutput('vlc')  

elif choice == '3' :
     # To search something on Google
     data=input("Type your favourite song:--->  ")
     webbrowser.open_new_tab('https://www.google.com/search?q='+data)

elif choice == '4' :
  # To connect os level application we use subprocess
     subprocess.getoutput('vlc')    # to text someone on whatsapp
     webbrowser.open_new_tab('https://api.whatsapp.com/send?phone=919511537588&text=Hiiii')

elif choice == '5' :
     # To connect our BIOS time
     current_time=time.ctime()
     print(current_time)

elif choice == '6' :
     # To reboot
     a="shutdown -h now" 
     process=subprocess.Popen(a.split(),stdout=subprocess.PIPE)
 
else :
     print("helloo")

