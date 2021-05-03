import slackNotification as slack
import tools.EditFile as file
import tools.GetServerStatus as status
import serverNotification as server
import datetime

keyDir= "/keys"

def checkServerStatus():
	
	#get ServerStatus
	ServerStatus = status.ServerStatus()
	MemoryFree = ServerStatus.getMemoryFree()
	CpuUsage = ServerStatus.getCpuPercent()

	#get setting from config
	FileHandle=file.File(keyDir,"envConfig.json")
	data = FileHandle.ReadFile()
	MemoryFreeAlarm=data["Alarm"]["MemoryFreeAlarm"]
	MemoryAlarmStatus=data["Alarm"]["Status"]

	
	Status = {}
	Status["MemoryFree"] = MemoryFree
	Status["CpuUsage"] = CpuUsage

	#send message to server
	server.sendToServer(Status)

	#create Status for slack
	if MemoryFree < MemoryFreeAlarm:
		Status["Alarm"] = True
	else:
		Status["Alarm"] = False
	print(str(datetime.datetime.now()) + " "  + str(Status))
	if Status["Alarm"] != MemoryAlarmStatus:
		FileHandle=file.File(keyDir,"envConfig.json")
		Slackdata = FileHandle.ReadFile()
		Slackdata["Alarm"]["Status"] = Status["Alarm"]
		FileHandle.UpdateFile(Slackdata)
		slack.sendMessage(Status)
	return Status
	

if __name__ == '__main__':
	#Result=Caculate(**Memory)
	#print(Result)
	checkServerStatus()
