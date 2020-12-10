import requests
import fs
from fs import open_fs
import sys

def getWebHook():
	with open_fs('../keys') as home_fs:
		with home_fs.open('slackWebhook.txt') as webhook_key:
			slackWebHook=webhook_key.read()
			print(slackWebHook)
			return slackWebHook

def setMessage(status):
	#with open_fs('../shell') as home_fs:
	with open_fs('.') as home_fs:
		with home_fs.open('sampleNotification.json') as Message:
			print(status)
			slackMessage=Message.read()
			return slackMessage	

def sendMessage(status):
	url = getWebHook()
	payload = setMessage(status)
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post(url, data=payload, headers=headers)
	print(r.status_code)


