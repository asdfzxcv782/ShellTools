import requests
import fs
import json
from fs import open_fs
import sys
import socket
import os

print(os.getenv('shelltools_path'))

def getWebHook():
	with open_fs('../keys') as home_fs:
		with home_fs.open('slackWebhook.txt') as webhook_key:
			slackWebHook=webhook_key.read()
			print(slackWebHook)
			return slackWebHook

def setMessage(status):
	#with open_fs('../py') as home_fs:
	with open_fs('.') as home_fs:
		with home_fs.open('sampleNotification.json') as Message:
			print(status)
			slackMessage=json.loads(Message.read())
			if status["Alarm"] == True :
				slackMessage["username"] = socket.gethostname()
				slackMessage["icon_emoji"] = ":x:"
				slackMessage["attachments"][0]["color"]= "#A0161E"
				slackMessage["attachments"][0]["fields"][0]["title"]="MemoryFree"
				slackMessage["attachments"][0]["fields"][0]["value"]=str(status["MemoryFree"]) + "%"
				slackMessage["attachments"][0]["fields"][1]["title"]="MemoryUsed"
				slackMessage["attachments"][0]["fields"][1]["value"]=str(status["MemoryUsed"]) + "%"
			else:
				slackMessage["icon_emoji"] = ":heavy_check_mark:"	
			print(slackMessage)
			return json.dumps(slackMessage,  indent=4)

def sendMessage(status):
	url = getWebHook()
	payload = setMessage(status)
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, data=payload, headers=headers)
	print(r.text)


