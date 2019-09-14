from playsound import playsound
import os
import re
#------------------------------------------------

def save_liste(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close


def load_list(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp=open(path,'r')
        l=fp.readlines()
        fp.close
        return(l)



#----------------main------------------
print('\n\n play.py')
piste=load_list("/tmp/music_to_play").pop(-1)
print(piste)
if (piste.replace("\n",'')==''):
    print ('wtf')
else:
    os.system("pwd")
    playsound(piste.replace("\n",''))
    pm_pids=load_list('/tmp/con_pid')
    pm_pid=pm_pids[0]
    pm_pid=re.findall('\d+', pm_pid)[0]
    print('playmuic_pid is :'+pm_pid)
    os.system('kill -9 '+pm_pid)
