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
        print("No internet connection available.")
    return False

instructionService.createMissingInstructions()
directoriesService.createMissingDirectories()
        


# if (connected_to_internet()==True):
#      time()
#      instruction()
