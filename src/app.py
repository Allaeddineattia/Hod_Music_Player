import slotManager
import sys
sys.path.insert(1, 'setup/')
import setup

from gtts import gTTS
from playsound import playsound
import os
from random import shuffle
import requests


class autoInstruct:
    value = False

def saveListe(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close
    
def loadList(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp=open(path,'r')
        l=fp.readlines()
        fp.close
        return(l)

def savePlaylist(play_liste):
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
    number = slotManager.getSlotNumberFromUser()
    while True:
        while (number == 5):
            slotManager.playHelpInstructionOfSavingSlot()
            number = slotManager.getSlotNumberFromUser()
        if (number == 0):
            slotManager.cancelPlaylistSaving()
        else :
            if (slotManager.savePlayListInSlot(number, play_liste)):
                break
            number = slotManager.getSlotNumberFromUser()
            



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
def playOptionInstruction():
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
def getSelectTrackOption():
    while True:
        try:
            x = int(input("1:take \n2:leave\n3:take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\ninput: "))
            return x
        except :
            print('please use a number')


def createList(musicList) :
    final=[]
    for trackPath in musicList:
        trackName = extractTrackNameFromTrackPath(trackPath)
        print(trackName)
        playsound("./music_mp3/name_" + trackName + ".mp3")
        selectTrackOption = getSelectTrackOption()
        while selectTrackOption not in (0,1,2,6,3) :
            if selectTrackOption == 4 :
                playsound("./music_mp3/name_"+trackName+".mp3")
            if selectTrackOption == 5 :
                playOptionInstruction()
            selectTrackOption = getSelectTrackOption()
        if selectTrackOption == 0 :
            return([])
        if selectTrackOption == 1 :
            final.append(trackPath)
        if selectTrackOption == 3 :
            dif=[var for var in musicList if var not in final]  
            shuffle(dif)
            final.extend(dif)
            break
        if selectTrackOption == 6 :
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
def pickSavedSlot():
    playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
    out=os.popen("ls -t ./saves").read()
    slots=out.split("\n")
    slots=slots[:-1]
    print("slots: ",slots)
    saved_number = slotManager.getSlotNumberFromUser()
    while ((str(saved_number)not in slots) or (saved_number == 5 ) or (saved_number == 0) ):
        if(saved_number==5):
            playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
            for slot in slots:
                playsound("/usr/lib/vocal_player/"+slot+".mp3")
        if (saved_number==0) :
            playsound('/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3')
            break
        if (str(saved_number)not in slots):
            playsound('/usr/lib/vocal_player/instruction/slot_not_found.mp3')
            print("!!! slot not found !!!")
        saved_number = slotManager.getSlotNumberFromUser()
    return(loadList('./saves/'+str(saved_number)))


#------------------fct pour extraire le tag name et le artisite d'apres un fichier mp3---------------------
def getTag(pistePath):
    title=""
    pistePath=adapt_chaine(pistePath)
    title=os.popen("mp3info -p %t "+pistePath).read()
    artist=os.popen("mp3info -p %a "+pistePath).read()
    if (title!=""):
        if (artist!=""):
            return(title+" by "+artist)
    return(title)

#------- obtention des paths du piste musicaux

def listMusicInMusicDirectory() : 
    music_founded=os.popen("find ./music -type f -iname \"*.mp3\" -printf \"%CY %Cj %CT  %p \n\" | sort -r -k1,1 -k2,2  -k3,3 | cut -d \  -f5-").read()
    music_founded=music_founded.split('\n')
    music_founded=music_founded[:-1]
    for i in range(len(music_founded)):
        music_founded[i]=music_founded[i][:-1]
    return music_founded

def findMusicTracks():
    music_founded = listMusicInMusicDirectory()
    if (music_founded==[]):
        print('no music founded')
        exit(4)
    return(music_founded)

#------- creation des fichiers mp3 contenants les noms des pistes trouver
def extractTrackNameFromTrackPath(trackPath):
    trackPath = trackPath.split("/")
    pisteName = trackPath[-1]
    pisteName = pisteName.replace(".mp3","")
    return pisteName

def getFileContaint(pisteTag, pisteName):
    containt = pisteTag
    if (pisteTag == ""):
        containt = pisteName.replace("_"," ")
    return (containt.replace(".mp3", ""))

def tryCreateMp3File (path, fileContent):
    if not(os.path.exists(path)):
        if (setup.connected_to_internet):
            string=gTTS(text = fileContent, lang='en')
            string.save(path)
            return 0 
        else:
            return 1
    return 0
    
def createTrackNameFilePath ( name):
    return "./music_mp3/name_" + name + ".mp3"

def createMp3FilesContainingTrackNames(musicFounded):
    missingFile=0
    for pistePath in musicFounded :
        pisteTag = getTag(pistePath)
        pisteName = extractTrackNameFromTrackPath(pistePath)
        fileContent = getFileContaint(pisteTag, pisteName)
        filePath = createTrackNameFilePath( pisteName)
        fileIsMissing = tryCreateMp3File(filePath, fileContent)
        missingFile += fileIsMissing 
    print(str(missingFile)+" track is missing")

#----------------- get auto instruction option
def initAutoInstruction():
    playsound('/usr/lib/vocal_player/instruction/on.mp3')
    while True:
        try:
            option=int(input('5 to automatic\ninput: '))
            break
        except:
            print("use a number please")
    if(option==5):
        autoInstruct.value=True

def playWelcomeInstruction():
    playsound('/usr/lib/vocal_player/welcome_to_vocale.mp3')

def playInstructionsAfterInitialistingAutoInstruction():
    playsound('/usr/lib/vocal_player/instruction/first.mp3')
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/auto_on.mp3')
    else:
        playsound('/usr/lib/vocal_player/instruction/auto_off.mp3')
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/create.mp3')


def getMusicToPlayInitializationOptionFromUser():
    while True:
        try:
            op = int(input("0:exit\n1:create a list\n2:chose a saved list\n5:instructions\ninput: "))
            return (op)
        except :
            print('please use a number ')


def initMusicToPlayInitializationOption():
    op = 5
    while op not in (0,2,1):
        op = getMusicToPlayInitializationOptionFromUser()
        if (op == 5):
            playsound('/usr/lib/vocal_player/instruction/help.mp3')
            op = getMusicToPlayInitializationOptionFromUser()
            if (op == 5):
                playsound('/usr/lib/vocal_player/instruction/create.mp3')
            else:
                playsound('/usr/lib/vocal_player/instruction/create_'+str(op)+'.mp3')
            op = 5
    return (op)


def createNewPlayList():
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    if (autoInstruct.value):
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')
    musicToPlay = createList(musicFounded)
    musicToPlay = musicToPlay[::-1]
    x='\n\t'.join(musicToPlay)
    musicToPlay=x.split('\t')
    playsound('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')
    while True:
        try:
            saveOption=int(input('1: save\ninput: '))
            break
        except:
            print('please a number')
    if (saveOption == 1):
        playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
        savePlaylist(musicToPlay)
    return musicToPlay

def initMusicToPlay( option):
    if option == 0:
        exit(-4)
    if option == 1:
        musicToPlay = createNewPlayList()
        return (musicToPlay)
    if option == 2:
        return (pickSavedSlot())

#---------les piles des piste musicaux
def printMusicToBePlayed(musicToPlay):
    print("\nMusic to be played:\n")
    for musicTrack in musicToPlay:
        print(musicTrack)


music_played = []
musicFounded = findMusicTracks()
playWelcomeInstruction()
createMp3FilesContainingTrackNames(musicFounded)
initAutoInstruction()
playInstructionsAfterInitialistingAutoInstruction()

musicToPlayInitializationOption = initMusicToPlayInitializationOption()
musicToPlay = initMusicToPlay(musicToPlayInitializationOption)
    
saveListe(musicToPlay,'/tmp/music_to_play')
printMusicToBePlayed(musicToPlay)


if (autoInstruct.value):
    playsound("/usr/lib/vocal_player/instruction/play.mp3")

while (os.path.getsize('/tmp/music_to_play') > 0):
    musicToPlay = loadList('/tmp/music_to_play')
    playMusic()

print('fin')
killall()
