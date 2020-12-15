import sys
import slackNotification as slack

Memory={
	"MemoryTotal":sys.argv[1],
	"MemoryUsed":sys.argv[2],
	"MemoryFree":sys.argv[3]
}

MemoryFreeAlarm=20

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
