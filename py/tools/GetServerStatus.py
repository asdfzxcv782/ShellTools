import psutil


class ServerStatus():
    def __init__(self):
        pass

    def getMemoryFree(self):
        Result=round((psutil.virtual_memory().free/psutil.virtual_memory().total*100),2)
        return Result

    def getDiskPartitions(self):
        return psutil.disk_partitions()

    def getCpuPercent(self):
        return psutil.cpu_percent(interval=1)

    def getPids(self):
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            print(proc.info)        
	
if __name__ == '__main__':
    Status=ServerStatus()
    print(Status.getMemoryFree())
    print(Status.getDiskPartitions())
    print(Status.getCpuPercent())  