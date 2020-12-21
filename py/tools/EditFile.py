import fs
from fs import open_fs
import json
class File():
    def __init__(self,FilePath,FileName):
        self.FilePath = FilePath
        self.FileName = FileName
        
    def Readjson(self):
        with open_fs(self.FilePath) as home_fs:
            with home_fs.open(self.FileName,'r') as envConfig:
                print("test")
                return json.load(envConfig)    
            envConfig.close()
        home_fs.close()

    def Updatejson(self,data):
        with open_fs(self.FilePath) as home_fs:
            with home_fs.open(self.FileName,'w') as envConfig:
                json.dump(data, envConfig)   
            envConfig.close()
        home_fs.close()
        
        
        


