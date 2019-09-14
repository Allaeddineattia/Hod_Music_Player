print('setup mode')
import os
import requests
import instructions as instructionService
import directories as directoriesService


def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("\nError: No internet connection available.\n")
        exit(-4)
    return False

def setupInstructions() : 
    while(instructionService.countMissingInstructions() !=0 ):
        print('there is '+str( instructionService.countMissingInstructions() )+' configuration file/s not found')
        if (connected_to_internet()):
            print('setup mode will be executed please wait...')
            instructionService.createMissingInstructions()

def setupDirectories() :
    directoriesService.createMissingDirectories()
        

def setup() :
    setupDirectories()
    setupInstructions()
    
setup()
