import os
from playsound import playsound

def saveListe(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close

def getSlotNumberFromUser():
    while True:
        try:
            number = input("0:exit \nelse exept 5\ninput: ")
            return number         
        except :
            print('please use a number.')

def playHelpInstructionOfSavingSlot():
    playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
    playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')

def cancelPlaylistSaving():
    playsound('/usr/lib/vocal_player/instruction/save_cancled.mp3')
    print("save cancled")

def askUserForOverridingSlot():
    while True:
        try:
            d = input('press one to override the old one\ninput: ')
            return d          
        except :
            print('please use a number.')

def savePlayListInSlot(slotNumber, play_list):
    d = 1
    if (os.path.exists('./saves/'+str(slotNumber))):
        playsound('/usr/lib/vocal_player/instruction/slot_exist.mp3')
        date_modification=os.popen("stat ./saves/"+str(slotNumber)+" |grep Modify |cut -d \  -f 2").read()
        heure_modification=os.popen("stat ./saves/"+str(slotNumber)+" |grep Modify |cut -d \  -f 3").read()
        print(date_modification)#months sound
        print(heure_modification)
        playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
        d = askUserForOverridingSlot()
    if d == 1:
        saveListe(play_list,'./saves/'+str(slotNumber))
        playsound('/usr/lib/vocal_player/instruction/save_succeeded.mp3')
        playsound('/usr/lib/vocal_player/'+str(slotNumber)+'.mp3')
        return (True)
    return (False)