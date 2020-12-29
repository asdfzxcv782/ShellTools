import os
import fs
from fs import open_fs
import json
import tools.EditFile as file

keyDir= "/keys"

def setEnv():
    passphrase=input("Passphrase: ")
    setPassphrase(passphrase)
    Alarm=input("MemoryFreeAlarm:")
    setMemoryFreeAlarm(int(Alarm))
    EncryptKey(passphrase)

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

def EncryptKey(passphrase):
    FIleHandle=file.File(keyDir)
    FIleHandle.EncyptFile(passphrase)
            

if __name__ == '__main__':
    setEnv()


