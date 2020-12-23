import psutil


class ServerStatus():
    def __init__(self):
        pass

    def getMemoryFree(self):
        return psutil.virtual_memory().percent
	
if __name__ == '__main__':
    Status=ServerStatus()
    print(Status.getMemoryFree())    