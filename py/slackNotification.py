import requests
import fs
import json
from fs import open_fs
import sys
import socket
import os
import tools.EditFile as file

#home=os.environ['HOME']
keyDir="/keys"

def getWebHook():
	FileHandle=file.File(keyDir,"slackWebhook.txt")
	data = FileHandle.ReadFile()
	return data
	

def setMessage(status):
	FileHandle=file.File(keyDir,"sampleNotification.json")
	slackMessage = FileHandle.ReadFile()
	if status["Alarm"] == True :
		slackMessage["icon_emoji"] = ":x:"
		slackMessage["attachments"][0]["color"]= "#A0161E"
	else:
		slackMessage["icon_emoji"] = ":heavy_check_mark:"
		slackMessage["attachments"][0]["color"]= "#36a64f"
	slackMessage["username"] = socket.gethostname()	
	slackMessage["attachments"][0]["fields"][0]["title"]="MemoryFree"
	slackMessage["attachments"][0]["fields"][0]["value"]=str(status["MemoryFree"]) + "%"
	slackMessage["attachments"][0]["fields"][1]["title"]="CpuUsed"
	slackMessage["attachments"][0]["fields"][1]["value"]=str(status["CpuUsage"]) + "%"	
	return json.dumps(slackMessage,  indent=4) 

def sendMessage(status):
	url = getWebHook()
	payload = setMessage(status)
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, data=payload, headers=headers)
	print(r.text)
	
if __name__ == '__main__':
	Status={
		"Alarm":False,
		"MemoryFree":60,
		"MemoryUsed":40
	}
	sendMessage(Status)