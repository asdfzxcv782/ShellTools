import sys
import os
import fs
from fs import open_fs
import json
import slackNotification as slack

Memory={
	"MemoryTotal":sys.argv[1],
	"MemoryUsed":sys.argv[2],
	"MemoryFree":sys.argv[3]
}

home=os.environ['HOME']
keyDir=home+"/ShellTools/keys"

with open_fs(keyDir) as home_fs:
	with home_fs.open('envConfig.json','r') as envConfig:
		data=json.load(envConfig)
		MemoryFreeAlarm=data["Alarm"]["MemoryFreeAlarm"]
	envConfig.close()
home_fs.close()		


def Caculate(**info):
	#MemoryFreeAlarm=90
	for index,x in enumerate(info,start=1):
		info[x]=int(sys.argv[index])
	Status={
		"Alarm":False,
		"MemoryFree":"",
		"MemoryUsed":""
	}
	print(Status)
	Status["MemoryFree"]=round((info["MemoryFree"]/info["MemoryTotal"]*100),2)
	Status["MemoryUsed"]=round((info["MemoryUsed"]/info["MemoryTotal"]*100),2)
	if Status["MemoryFree"] < MemoryFreeAlarm :
		Status["Alarm"]=True
	slack.sendMessage(Status)	
	return Status
	

Result=Caculate(**Memory)

print(Result)
