import psutil


class ServerStatus():
    def __init__(self):
        pass

    def getMemoryFree(self):
        Result=round((psutil.virtual_memory().free/psutil.virtual_memory().total*100),2)
        return Result
	
if __name__ == '__main__':
    Status=ServerStatus()
    print(Status.getMemoryFree())    