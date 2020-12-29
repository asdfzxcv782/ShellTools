import sys
import os
import fs
from fs import open_fs
import json
import slackNotification as slack
import tools.EditFile as file
import tools.GetServerStatus as status


home=os.environ['HOME']
keyDir=home+"/ShellTools/keys"
FileHandle=file.File(keyDir,"envConfig.json")
data = FileHandle.ReadFile()
MemoryFreeAlarm=data["Alarm"]["MemoryFreeAlarm"]
MemoryAlarmStatus=data["Alarm"]["Status"]

'''
def Caculate(**info):
	for index,x in enumerate(info,start=1):
		info[x]=int(sys.argv[index])
	Status={
		"Alarm":False,
		"MemoryFree":"",
		"MemoryUsed":""
	}
	print(Status)
	Status["MemoryFree"]=round((info["MemoryFree"]/info["MemoryTotal"]*100),2)
	if Status["MemoryFree"] < MemoryFreeAlarm :
		Status["Alarm"]=True
	print(MemoryAlarmStatus)	
	if Status["Alarm"] != MemoryAlarmStatus:
		FileHandle=file.File(keyDir,"envConfig.json")
		Slackdata = FileHandle.ReadFile()
		Slackdata["Alarm"]["Status"] = Status["Alarm"]
		FileHandle.UpdateFile(Slackdata)
		slack.sendMessage(Status)	
	return Status
'''
if __name__ == '__main__':
	#Result=Caculate(**Memory)
	print(Result)
