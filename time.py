from gtts import gTTS
import os
from datetime import datetime
from playsound import playsound 
 
if not(os.path.exists("/usr/lib/vocal_player")) :
	os.mkdir("/usr/lib/vocal_player",0755)
string=""
s=""

h=str(int(datetime.now().strftime('%H')))
m=str(int(datetime.now().strftime('%M')))
pid_file=open("/tmp/play_pid",'r')
playsound_pid=pid_file.readlines()
pid_file.close()
for i in playsound_pid:
    print(i)
    os.system("kill -19 "+i) 
if h=='0' or m=='0':
    if m=='0' and h=='0':
        playsound("/usr/lib/vocal_player/time.mp3")
        playsound("/usr/lib/vocal_player/midnight.mp3")
        #playsound("/usr/lib/vocal_player/"+m+".mp3")
    elif m=='0':
        playsound("/usr/lib/vocal_player/time.mp3")
        playsound("/usr/lib/vocal_player/"+h+".mp3")
        playsound("/usr/lib/vocal_player/clock.mp3")
    else:
        playsound("/usr/lib/vocal_player/time.mp3")
        playsound("/usr/lib/vocal_player/midnight.mp3")
        playsound("/usr/lib/vocal_player/"+m+".mp3")
        playsound("/usr/lib/vocal_player/minute.mp3")
else:
    playsound("/usr/lib/vocal_player/time.mp3")
    playsound("/usr/lib/vocal_player/"+h+".mp3")
    playsound("/usr/lib/vocal_player/"+m+".mp3")
    playsound("/usr/lib/vocal_player/minute.mp3")
for i in playsound_pid :
    print(i)
    os.system("kill -18 "+i)