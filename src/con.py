import os
import re
from playsound import playsound

def initProcessesId():
    os.system("ps |grep python >/tmp/vocal_pid")
    os.system("ps -eo pid,tty,time,cmd |grep con.py$|grep -f \"/tmp/vocal_pid\" >/tmp/con_pid")
    os.system("ps -eo pid,tty,time,cmd |grep play.py$|grep -f \"/tmp/vocal_pid\" >/tmp/play_pid")
    pid_file = open("/tmp/play_pid",'r')
    playsoundPid = pid_file.readlines()
    pid_file.close()
    return playsoundPid
    
#------------------------------------------------
def saveList(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close


def loadList(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp = open(path,'r')
        result = fp.readlines()
        fp.close
        return(result)

#--------------option0------------------------
def stop (playsoundPid):
    stringToExecute=''
    for pid in playsoundPid :
        pid=re.findall('\d+', pid)[0]
        stringToExecute+='kill '+pid+' ;'
    stringToExecute=stringToExecute[0:-1]
    os.system(stringToExecute)   
    
#--------------option1------------------------
def pause (playsoundPid):
    stringToExecute=''
    for pid in playsoundPid :
        pid=re.findall('\d+', pid)[0]
        stringToExecute+="kill -19 "+pid+' ;'
    stringToExecute=stringToExecute[0:-1]
    os.system(stringToExecute)
    print(stringToExecute)

#--------------option2------------------------
def resume (playsoundPid):
    stringToExecute=''
    for pid in playsoundPid :
        pid=re.findall('\d+', pid)[0]
        #print(pid)
        stringToExecute+="kill -18 "+pid+' ;'
    stringToExecute=stringToExecute[0:-1]
    os.system(stringToExecute)
    print(stringToExecute)  
#a=int(input("options:\n 0:stop \n 1:pause \n 2:resume \n 3:volume down \n 6:volume up   \n 9:next \n 7:prec\n"))

#--------------option7------------------------
def prev(music_to_play , music_played):
    if (not(len(music_played)==0)):    
        a=music_played.pop(-1)
        #play_music(a)
        print("the prev is"+a)
        music_to_play.append(a)
        if (not(len(music_played)==0)):    
            a=music_played.pop(-1)
            #play_music(a)
            print("the prev is"+a)
            music_to_play.append(a)
        saveList(music_played,'/tmp/music_played')
        saveList(music_to_play,'/tmp/music_to_play')
    else:
         print('no prev')

#--------------option0------------------------
def killall():
    f=open("/tmp/vocal_pid",'r')
    l=f.readlines()
    f.close()
    f=open("/tmp/music_played",'w')
    f.write("")
    f.close()
    for i in l :
        os.system("kill -9 "+i)

 
def playOption():
    pause(playsoundPid)
    playsound('/usr/lib/vocal_player/instruction/help.mp3')
    op=input()
    if(op in (0,1,2,3,4,6,7,8,9)):
        playsound('/usr/lib/vocal_player/instruction/play_'+str(op)+'.mp3')
    else:
        playsound('/usr/lib/vocal_player/instruction/play.mp3')
    resume (playsoundPid)

def volume(v_op):
    #----------------determiniation des caracteristiques de son_input de python----------
    s="pactl list sink-inputs|grep -e Sink\ Input -e application.name\ =\ \\\"python\\\" -e Volume| grep -B 2 python"
    print("\n")
    out=os.popen(s).read()
    #----------------determination de volume intiale-------------------------------------
    volume=os.popen("echo \""+out+"\"|grep Volume | cut -d / -f 2").read()
    volume=re.findall('\d+', volume)[0]
    x=int(volume)
    #----------------determination du sink number----------------------------------------
    sink=os.popen("echo \""+out+"\"|grep Sink | cut -d \\# -f 2").read()
    sink=re.findall('\d+', sink)[0]
    #----------------diminution de volume------------------------------------------------
    if (v_op==3 and x>0):
        x-=5
    #----------------augmentation de volume----------------------------------------------
    if (v_op==6 and x<100):
        x+=5
    if (v_op==7):
        if(x>0):
            x=0
        else:
            x=50
    #----------------excution du commande------------------------------------------------
    os.system("pactl set-sink-input-volume "+sink+" "+str(x)+"%") 

#----------------------------main--------------------


playsoundPid = initProcessesId()
music_to_play = loadList('/tmp/music_to_play')
music_played = loadList('/tmp/music_played')

music_played.append(music_to_play.pop(-1))
saveList(music_played,'/tmp/music_played')
saveList(music_to_play,'/tmp/music_to_play')

x=0

def getUserInputOption() :
    while True:
        try:
            result = int(input('options:\n 0:stop \n 2:pause\\resume  \n 3:next \n 1:prec \n 6:volume down \n 9:volume up \n 7:mute\unmute \n 8:time  \n 5:instruction\ninput: '))
            return result
        except :
            print("plz use a number.")

def managingPlayListByuserInput( ) : 
    userInputOption = getUserInputOption();
    while (True):
        if userInputOption == 3 :
            stop(playsoundPid)
            break
        elif userInputOption == 2 :
            if (x==0):
                pause(playsoundPid)
                x=1
            else:
                resume (playsoundPid)
                x=0
        elif userInputOption == 7 :
            volume(7)
        elif userInputOption == 9 :
            volume(6)
        elif userInputOption == 1 :
            if (not(len(music_played)==0)):
                prev(music_to_play , music_played)
                stop(playsoundPid)
                break
            else : print("there's no prev")
        elif userInputOption == 6 :
            volume(3)
        elif userInputOption == 0 :
            killall() 
        elif userInputOption == 8:
            os.system("python time.py")  
        elif userInputOption == 5:
            playOption()
        userInputOption = getUserInputOption();
        
managingPlayListByuserInput()