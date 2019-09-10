
from gtts import gTTS
import os

instructions = []


def initInstructions() : 
    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/minute.mp3",
            "text": "minute"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/time.mp3",
            "text": "the time is"
        }
        )

    for i in range(1, 61) :
        s = str(i)
        instructions.append(
            {
                "path":  "/usr/lib/vocal_player/"+s+".mp3",
                "text": s
            }
            )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/midnight.mp3",
            "text": "midnight"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/clock.mp3",
            "text": "o'clock"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/welcome_to_vocale.mp3",
            "text": "welcome to C L L vocale music player."
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/on.mp3",
            "text": "press 5 to start the qutomatic guidance\n highly recomanded if this your first use"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/first.mp3",
            "text": "If you're blocked press 5 for help."
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/create.mp3",
            "text": "press 0 to exit the program \n press 1 to create new list \n or press 2 to chose a saved listes"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/create_0.mp3",
            "text": "exit the program"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/create_1.mp3",
            "text": "create new list"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/create_2.mp3",
            "text": "chose between saved listes"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option.mp3",
            "text": "press 0 to exit the program \npress 1 to add to list\npress 2 to ignore \npress 3 to add all the rest\n press 4 to rehear the name \n 6 to end selection"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_0.mp3",
            "text": "exit the program"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_1.mp3",
            "text": "add the track"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_2.mp3",
            "text": "skip to next track"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_3.mp3",
            "text": "add all the rest to playlist"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_4.mp3",
            "text": "rehear the name"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/creation_option_6.mp3",
            "text": "end selection"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play.mp3", 
            "text": "press 0 to exit \npress 2 to pause and resume  \npress 3 to skip to next \npress 1 to back to previous  \npress 6 to volume down \npress 9 to volume up \npress 7 to mute\unmute \npress 8 to hear time  \n"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_0.mp3",
            "text": " exit the program \n"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_2.mp3",
            "text": "pause and resume "
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_3.mp3",
            "text": "skip to next"
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_1.mp3",
            "text": " back to previous "
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_6.mp3",
            "text": "lower the volume "
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_9.mp3",
            "text": "volume up "
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_8.mp3",
            "text": " hear time "
        }
        )

    instructions.append(
        {
            "path":  "/usr/lib/vocal_player/instruction/play_7.mp3",
            "text": " mute unmute"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/save_playlist_option.mp3',
            "text": " press 1 to save the list"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/save_playlist.mp3',
            "text": " Chose a slot from 1 to 9 exept the 5 wich remain used for help or use 0 to cancel"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/save_cancled.mp3',
            "text": "your playlist will not be saved"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/save_succeeded.mp3',
            "text": "playlist saved in slot number "
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/auto_on.mp3',
            "text": "auto guidance is on"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/auto_off.mp3',
            "text": "auto guidance is off"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/save_playlist_mode.mp3',
            "text": "you are about to save your playlist"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/creation_mode.mp3',
            "text": "you are about to create a playlist"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/help.mp3',
            "text": "repress 5 to hear all instruction or press one of the other buttons to hear it funcionality"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/slot_exist.mp3',
            "text": "slot exist already"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3',
            "text": "pick saved cancled"
        }
        )

    instructions.append(
        {
            "path":  '/usr/lib/vocal_player/instruction/pick_saved.mp3',
            "text": "chose a slot"
        }
        )


def handleError(err):
    print(err)
    print('\n!!!!!!!\nsuper user mode is needed.\nre-execute the program as superuser.\nsudo python main.py\n!!!!!!!!\n')
    exit(0)


def checkFileEmptiness(path):
    if (os.path.getsize(path) == 0): 
        print(path+ " file is empty")
        try : 
            os.system("sudo rm "+path)
            return (1)
        except Exception as err :
            handleError(err)
    else:
        print(path + " checked")
        return (0)


def checkMissingFile(path):
    if not (os.path.exists(path)):
        print(path+ " file is missing")
        return(1)
    else :
        return(checkFileEmptiness(path))

def countMissingInstructions(): 
    missingInstructions=0
    for instruction in instructions:
        missingInstructions += checkMissingFile(instruction.get(
                "path"))
    print ('the number of missing instructions is: ' + str (missingInstructions))
    return(missingInstructions)

def createInstruction( path, txt):
    print("creating "+ path)
    string=gTTS(text=txt, lang='en')
    try:
        string.save(path)
        print(path + " is created")
    except Exception as err:
        handleError(err)

def createMissingInstructions():
    for instruction in instructions: 
        path = instruction.get( "path")
        text = instruction.get( "text")
        if (checkMissingFile(path) == 1):
            createInstruction(path, text)

initInstructions()







