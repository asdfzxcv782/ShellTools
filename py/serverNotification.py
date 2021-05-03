import requests
import json
import tools.EditFile as file
import socket
from requests.auth import HTTPBasicAuth

def sendToServer(status):
    keyDir="/keys"
    FileHandle=file.File(keyDir,"ServerRequestConfig.json")
    status["userName"] = socket.gethostname()
    data = FileHandle.ReadFile()
    headers = {'Content-Type': 'application/json'}
    r = requests.post(data['url'], data=json.dumps(status,  indent=4), headers=headers, auth=HTTPBasicAuth(data['name'], data['password']))
    print("response: " + r.text)
