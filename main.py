try : 
    import setup
except Exception as err:
    print(err)
    print('\n!!!!!!!\nsuper user mode is needed.\nre-execute the program as superuser.\nsudo python main.py\n!!!!!!!!')
    exit(0)
from gtts import gTTS
from playsound import playsound
import os
from random import shuffle
import requests


class autoInstruct:
    value=False
#------------------verification de l'existance des fichiers setup---------------------
def checkCreatedInstruction(path):
    if not (os.path.exists(path)):
        print(path+ " missing")
        return(1)
    else :
        if (os.path.getsize(path) == 0): 
            print(path+ " not created well")
            try : 
                os.system("sudo rm "+path)
            except :
                print('\n!!!!!!!\nsuper user mode is needed.\nre-execute the program as superuser.\nsudo python main.py\n!!!!!!!!')
                exit(0)

            return(1)
    print(path + ' is cheked.')
    return(0)

def missingInstruction():
    missingInstructions=0
    paths=setup.getPaths()
    for path in paths:
        missingInstructions  += checkCreatedInstruction(path)
    for i in range (1,61):
        s=str(i)
        missingInstructions += checkCreatedInstruction("/usr/lib/vocal_player/"+s+".mp3")
    return(missingInstructions)

#----------------verification des dossiers du sauvgarde






#------------------fct pour sauvgarder une liste dans fichier---------------------
def saveListe(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close


#------------------fct pour sauvgarder une liste dans un slots---------------------
#sauvegarde dans the least aded
def savePlaylist(play_liste):
    existsSlots=os.popen("ls ./saves")
    
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
    

    
    while True:
        try:
            number=input("0:exit \nelse exept 5\ninput: ")
            break           
        except :
            print('please use a number.')
    
    while True:
        d=1
        while (number==5):
            playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
            playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
            while True:
                try:
                    number=input("0:exit \n else exept 5\ninput: ")
                    break           
                except :
                    print('please use a number.')
        
        if (number==0):
            playsound('/usr/lib/vocal_player/instruction/save_cancled.mp3')
            print("save cancled")
            break
        else :
            if (os.path.exists('./saves/'+str(number))):
                playsound('/usr/lib/vocal_player/instruction/slot_exist.mp3')
                date_modification=os.popen("stat ./saves/"+str(number)+" |grep Modify |cut -d \  -f 2").read()
                heure_modification=os.popen("stat ./saves/"+str(number)+" |grep Modify |cut -d \  -f 3").read()
                print(date_modification)#months sound
                print(heure_modification)
                playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
                while True:
                    try:
                        d=input('press one to ecrase the old one\ninput: ')
                        break           
                    except :
                        print('please use a number.')
                
            if d==1:
                saveListe(play_liste,'./saves/'+str(number))
                playsound('/usr/lib/vocal_player/instruction/save_succeeded.mp3')
                playsound('/usr/lib/vocal_player/'+str(number)+'.mp3')
                break
            while True:
                try:
                    number=input("0:exit \n else exept 5\ninput: ")
                    break           
                except :
                    print('please use a number.')

#------------------fct pour charger une liste---------------------
def loadList(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp=open(path,'r')
        l=fp.readlines()
        fp.close
        return(l)

#------------------fct pour fermer le programme---------------------
def killall():
    f=open("/tmp/ps_pid",'r')
    l=f.readlines()
    f.close()
    f=open("/tmp/music_played",'w')
    f.write("")
    f.close()
    for i in l :
        os.system("kill -9 "+i)

#------------------fct pour ecouter les instruction de la creation d'une liste ---------------------
def createOptionInstruction():
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    playsound('/usr/lib/vocal_player/instruction/help.mp3')
    while True:
        try:
            op=input()
            break           
        except :
            print('please use a number.')
    
    if(op in (0,1,2,3,4,6)):
        playsound('/usr/lib/vocal_player/instruction/creation_option_'+str(op)+'.mp3')
    else:
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')

#------------------fct pour creer une liste --------------------------------------------------------  
def createList(musicList) :
    final=[]
    for originTrackPath in musicList:
        trackPath=originTrackPath.split("/")
        trackName=trackPath[-1]
        trackName=trackName.replace(".mp3","")
        print(trackName)
        playsound("./music_mp3/name_"+trackName+".mp3")
        while True:
            try:
                x=int(input("1:take \n2:leave\n3:take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\ninput: "))
                break           
            except :
                print('please use a number')
        while x not in (0,1,2,6,3) :
            if x==4 :
                playsound("./music_mp3/name_"+trackName+".mp3")
            if x==5 :
                createOptionInstruction()
            while True:
                try:
                    x=int(input("1:take \n2:leave\n3:take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\n"))
                    break           
                except :
                    print('please use a number')
        if x==0 :
            return([])
        if x==1 :
            final.append(originTrackPath)
        if x==3 :
            dif=[var for var in musicList if var not in final]  
            shuffle(dif)
            final.extend(dif)
            break
        if x==6 :
            break
    return(final)

#------------------fct pour adapter une chaine de caractere a le shell  ---------------------
def adapt_chaine(chaine):
    liste_des_carac_special=[' ','"','/','<','>','|',':','&','-',"(",")","'"]
    for i in liste_des_carac_special:
        chaine=chaine.replace(i,'\\'+i)
    chaine=chaine.replace('\n','')
    return(chaine)

#------------------fct pour ecouter un fichier mp3  ---------------------
def playMusic():
    os.system("python play.py & python con.py ")

#------------------fct pour choisir un slot  ---------------------
def pickSaved():
    playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
    out=os.popen("ls -t ./saves").read()
    slots=out.split("\n")
    slots=slots[:-1]
    print("slots: ",slots)
    while True:
        try:
            saved_number=input()
            break
        except :
            print('use a number')
    
    while ((str(saved_number)not in slots) or (saved_number==5) or (saved_number==0) ):
        if(saved_number==5):
            playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
            for slot in slots:
                playsound("/usr/lib/vocal_player/"+slot+".mp3")
        if (saved_number==0) :
            playsound('/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3')
            break
        if (str(saved_number)not in slots):
            #playsound('/usr/lib/vocal_player/instruction/slot_not_found.mp3')
            print("!!! slot not found !!!")
        while True:
            try:
                saved_number=input()
                break
            except :
                print('use a number')
    return(loadList('./saves/'+str(saved_number)))


#------------------fct pour extraire le tag name et le artisite d'apres un fichier mp3---------------------
def getTag(pistePath):
    title=""
    # print("before "+pistePath)
    pistePath=adapt_chaine(pistePath)
    # print("after "+pistePath)
    title=os.popen("mp3info -p %t "+pistePath).read()
    artist=os.popen("mp3info -p %a "+pistePath).read()
    if (title!=""):
        if (artist!=""):
            return(title+" by "+artist)
    return(title)

#------- obtention des paths du piste musicaux
def findMusicTrack():
    music_founded=os.popen("find ./music -type f -iname \"*.mp3\" -printf \"%CY %Cj %CT  %p \n\" | sort -r -k1,1 -k2,2  -k3,3 | cut -d \  -f5-").read()
    music_founded=music_founded.split('\n')
    music_founded=music_founded[:-1]
    for i in range(len(music_founded))  :
        music_founded[i]=music_founded[i][:-1]
    return(music_founded)

#------- creation des fichiers mp3 contenants les noms des pistes trouver
def createTrackName(musicFounded):
    missingFile=0
    for pistePath in musicFounded :
        pisteTag=getTag(pistePath)
        pistePath=pistePath.split("/")
        pisteName=pistePath[-1]
        pisteName=pisteName.replace(".mp3","")
        if (pisteTag==""):
            pisteTag=pisteName.replace("_"," ")
        if not(os.path.exists("./music_mp3/name_"+pisteName+".mp3")):
            if (setup.connected_to_internet):
                string=gTTS(text=pisteTag.replace(".mp3",""), lang='en')
                string.save("./music_mp3/name_"+pisteName+".mp3")
            else:
                missingFile+=1
    print(str(missingFile)+" track is missing")

#----------------- get auto instruction option
def autoInstruction():
    playsound('/usr/lib/vocal_player/instruction/on.mp3')
    while True:
        try:
            option=int(input('5 to automatic\ninput: '))
            break
        except:
            print("use a number please")
    if(option==5):
        autoInstruct.value=True

#---------------------------------------------------------------------
#--------------------main------------------------------------------------
#-----------------------------------------------------------------------

# --------------------verification des fichier system

while(missingInstruction()!=0):
    print('there is '+str(missingInstruction())+' configuration file/s not found')
    if (setup.connected_to_internet()):
        print('setup mode will be executed please wait...')
        try:
            setup.time()
            setup.instruction()
        except :
            print('\n!!!!!!!\nsuper user mode is needed.\nre-execute the program as superuser.\nsudo python main.py\n!!!!!!!!')
            exit(0)

    else:
        print('internet conection is needed')
        exit(-4)

print('all needed files exists')
#----------------message de reciption

playsound('/usr/lib/vocal_player/welcome_to_vocale.mp3')



#---------les piles des piste musicaux

musicToPlay=[]
music_played=[]


musicFounded=findMusicTrack()
if (musicFounded==[]):
    print('no music founded')
    exit(4)
createTrackName(musicFounded)
autoInstruction()


playsound('/usr/lib/vocal_player/instruction/first.mp3')



if (autoInstruct.value):
    playsound('/usr/lib/vocal_player/instruction/auto_on.mp3')
else:
    playsound('/usr/lib/vocal_player/instruction/auto_off.mp3')

if (autoInstruct.value):
    playsound('/usr/lib/vocal_player/instruction/create.mp3')



op=5
while op not in (0,2,1):
    while True:
        try:
            op=int(input("0:exit\n1:create a list\n2:chose a saved list\n5:instructions\ninput: "))
            break
        except :
            print('please use a number ')
    
    if (op==5):
        playsound('/usr/lib/vocal_player/instruction/help.mp3')
        while True:
            try:
                op=input("0:exit\n1:create a list\n2:chose a saved list\n5:instructions\ninput: ")
                break
            except :
                print ('use a number')
        
        if (op==5):
            playsound('/usr/lib/vocal_player/instruction/create.mp3')
        else:
            playsound('/usr/lib/vocal_player/instruction/create_'+str(op)+'.mp3')
        op=5


if op == 0:
    exit(-4)
if op == 1:
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')
    musicToPlay=createList(musicFounded)
    musicToPlay=musicToPlay[::-1]
    x='\n\t'.join(musicToPlay)
    musicToPlay=x.split('\t')
    playsound('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')
    while True:
        try:
            saveOption=int(input('1: save\ninput: '))
            break
        except:
            print('please a number')
    if (saveOption==1):
        playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
        
        savePlaylist(musicToPlay)

if op == 2:
    musicToPlay=pickSaved()
print("\nMusic to be played:\n")
for musicTrack in musicToPlay:
    print(musicTrack)

saveListe(musicToPlay,'/tmp/music_to_play')

if (autoInstruct.value):
    playsound("/usr/lib/vocal_player/instruction/play.mp3")

while (os.path.getsize('/tmp/music_to_play') > 0):
    musicToPlay=loadList('/tmp/music_to_play')
    playMusic()

print('fin')
killall()






        


    





