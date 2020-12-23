import requests
import fs
import json
from fs import open_fs
import sys
import socket
import os
import tools.EditFile as file

home=os.environ['HOME']
keyDir=home+"/ShellTools/keys"

def getWebHook():
	FileHandle=file.File(keyDir,"slackWebhook.txt")
	data = FileHandle.ReadFile()
	return data
	'''
	with open_fs(home + '/ShellTools/keys') as home_fs:
		with home_fs.open('slackWebhook.txt') as webhook_key:
			slackWebHook=webhook_key.read()
			print(slackWebHook)
			return slackWebHook
		webhook_key.close()
	home_fs.close()
	'''	

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
	slackMessage["attachments"][0]["fields"][1]["title"]="MemoryUsed"
	slackMessage["attachments"][0]["fields"][1]["value"]=str(status["MemoryUsed"]) + "%"	
	print(slackMessage)
	return json.dumps(slackMessage,  indent=4) 
	'''
	with open_fs(home + '/ShellTools/keys') as home_fs:
		with home_fs.open('sampleNotification.json') as Message:
			print(status)
			slackMessage=json.loads(Message.read())
			if status["Alarm"] == True :
				slackMessage["icon_emoji"] = ":x:"
				slackMessage["attachments"][0]["color"]= "#A0161E"
			else:
				slackMessage["icon_emoji"] = ":heavy_check_mark:"
				slackMessage["attachments"][0]["color"]= "#36a64f"
			slackMessage["username"] = socket.gethostname()	
			slackMessage["attachments"][0]["fields"][0]["title"]="MemoryFree"
			slackMessage["attachments"][0]["fields"][0]["value"]=str(status["MemoryFree"]) + "%"
			slackMessage["attachments"][0]["fields"][1]["title"]="MemoryUsed"
			slackMessage["attachments"][0]["fields"][1]["value"]=str(status["MemoryUsed"]) + "%"	
			print(slackMessage)
			return json.dumps(slackMessage,  indent=4)
		Message.close()
	home_fs.close()
	'''		

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