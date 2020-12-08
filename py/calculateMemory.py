import sys

Memory={
	"MemoryTotal":sys.argv[1],
	"MemoryUsed":sys.argv[2],
	"MemoryFree":sys.argv[3]
}


def Caculate(**info):
	for index,x in enumerate(info):
		#print(index)
		#print(x)
		info[x]=int(sys.argv[index + 1])
	return round((info["MemoryFree"]/info["MemoryTotal"])*100,2)
	

result=Caculate(**Memory)

print("Memory Free: "+ str(result) +" %")
