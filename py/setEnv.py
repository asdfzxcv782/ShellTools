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
    data = FIleHandle.Readjson()
    data["encrypt"]["passphrase"]=passphrase
    FIleHandle.Updatejson(data)
    """ 
    with open_fs(keyDir) as home_fs:
        with home_fs.open('envConfig.json','r') as envConfig:
            data=json.load(envConfig)
        data["encrypt"]["passphrase"]=passphrase
        with home_fs.open('envConfig.json','w') as envConfig:
            json.dump(data, envConfig)
        envConfig.close()
    home_fs.close()
    """    
def setMemoryFreeAlarm(Alarm) :
    FIleHandle=file.File(keyDir,"envConfig.json")
    data = FIleHandle.Readjson()
    data["Alarm"]["MemoryFreeAlarm"]=Alarm
    FIleHandle.Updatejson(data)
    '''
    with open_fs(keyDir) as home_fs:
        with home_fs.open('envConfig.json','r') as envConfig:
            data=json.load(envConfig)
        data["Alarm"]["MemoryFreeAlarm"]=Alarm
        with home_fs.open('envConfig.json','w') as envConfig:
            json.dump(data, envConfig)
        envConfig.close()
    home_fs.close()    
    '''
setEnv()            




