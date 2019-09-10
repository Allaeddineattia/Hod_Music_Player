import os

readOnlyDirectories = [
    "./music_mp3",
    "./saves",
    "/usr/lib/vocal_player",
    "/usr/lib/vocal_player/instruction"
]
writeAccesibleDirectories = [
    "./music",
]

def handleError(err):
    print(err)
    print('\n!!!!!!!\nsuper user mode is needed.\nre-execute the program as superuser.\nsudo python main.py\n!!!!!!!!\n')
    exit(0)

def createReadOnlyDirectory( path):

    print(path + " directory does not exist")
    try :
        os.mkdir(path,0755)
    except Exception as err:
        handleError(err)
    print(path + " is created")

def createWriteAccesibleDirectory( path):
    print(path + " directory does not exist")
    try:
        os.mkdir(path, 0755)
        os.chmod(path, 0777)
    except Exception as err:
        handleError(err)
    print(path + " is created")


def createMissingDirectories():
    print("creating missing repositorys")
    for directory in readOnlyDirectories:
        if not(os.path.exists(directory)):
            createReadOnlyDirectory( directory)
    for directory in writeAccesibleDirectories:
        if( os.path.exists(directory)):
            createWriteAccesibleDirectory( directory)

def countMissingDirecroties():
    missedDirectory = 0
    for directory in readOnlyDirectories:
        if not(os.path.exists(directory)):
            missedDirectory +=1
    for directory in writeAccesibleDirectories:
        if( os.path.exists(directory)):
            missedDirectory +=1
    return missedDirectory

print(countMissingDirecroties())