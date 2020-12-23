import sys
import os
import fs
from fs import open_fs
import json
import slackNotification as slack
import tools.EditFile as file

Memory={
	"MemoryTotal":sys.argv[1],
	"MemoryUsed":sys.argv[2],
	"MemoryFree":sys.argv[3]
}

home=os.environ['HOME']
keyDir=home+"/ShellTools/keys"
FileHandle=file.File(keyDir,"envConfig.json")
data = FileHandle.ReadFile()
MemoryFreeAlarm=data["Alarm"]["MemoryFreeAlarm"]
MemoryAlarmStatus=data["Alarm"]["Status"]
'''
with open_fs(keyDir) as home_fs:
	with home_fs.open('envConfig.json','r') as envConfig:
		data=json.load(envConfig)
		MemoryFreeAlarm=data["Alarm"]["MemoryFreeAlarm"]
		MemoryAlarmStatus=data["Alarm"]["Status"]
	envConfig.close()
home_fs.close()		
'''

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
	print(MemoryAlarmStatus)	
	if Status["Alarm"] != MemoryAlarmStatus:
		FileHandle=file.File(keyDir,"envConfig.json")
		Slackdata = FileHandle.ReadFile()
		Slackdata["Alarm"]["Status"] = Status["Alarm"]
		FileHandle.UpdateFile(Slackdata)
		'''
		with open_fs(keyDir) as home_fs:
			with home_fs.open('envConfig.json','r') as envConfig:
				data=json.load(envConfig)
				data["Alarm"]["Status"] = Status["Alarm"]
			with home_fs.open('envConfig.json','w') as envConfig:
				json.dump(data, envConfig)	
			envConfig.close()
		home_fs.close()
		'''	
		slack.sendMessage(Status)	
	return Status
	
if __name__ == '__main__':
	Result=Caculate(**Memory)
	print(Result)
