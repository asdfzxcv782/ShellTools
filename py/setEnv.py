import os
import fs
from fs import open_fs
import json
import tools.EditFile as file

home=os.environ['HOME']

keyDir=home+"/ShellTools/keys"

def setEnv():
    passphrase=input("Passphrase: ")
    setPassphrase(passphrase)
    Alarm=input("MemoryFreeAlarm:")
    setMemoryFreeAlarm(int(Alarm))

def setPassphrase(passphrase):
    FIleHandle=file.File(keyDir,"envConfig.json")
    data = FIleHandle.ReadFile()
    data["encrypt"]["passphrase"]=passphrase
    FIleHandle.UpdateFile(data)
    
def setMemoryFreeAlarm(Alarm) :
    FIleHandle=file.File(keyDir,"envConfig.json")
    data = FIleHandle.ReadFile()
    data["Alarm"]["MemoryFreeAlarm"]=Alarm
    FIleHandle.UpdateFile(data)
            

if __name__ == '__main__':
    setEnv()


