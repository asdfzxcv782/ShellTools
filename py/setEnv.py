import os
import fs
from fs import open_fs
import json

home=os.environ['HOME']

keyDir=home+"/ShellTools/keys"

def setEnv():
    passphrase=input("Passphrase: ")
    setPassphrase(passphrase)

def setPassphrase(passphrase): 
    with open_fs(keyDir) as home_fs:
        with home_fs.open('envConfig.json','r') as envConfig:
            data=json.load(envConfig)
        data["encrypt"]["passphrase"]=passphrase
        with home_fs.open('envConfig.json','w') as envConfig:
            json.dump(data, envConfig)
        envConfig.close()    




