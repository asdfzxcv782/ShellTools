import os
import fs
from fs import open_fs
import gnupg
import json

class File():
    def __init__(self,FilePath,FileName):
        ProjectPath = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
        self.FilePath = ProjectPath + FilePath
        self.FileName = FileName

    def ReadFile(self):
        with open_fs(self.FilePath) as home_fs:
            with home_fs.open(self.FileName,'r') as envConfig:
                if ".json" in self.FileName:
                    return json.load(envConfig)
                else:
                    return envConfig.read()    
            envConfig.close()
        home_fs.close()    

    def UpdateFile(self,data):
        with open_fs(self.FilePath) as home_fs:
            with home_fs.open(self.FileName,'w') as envConfig:
                if ".json" in self.FileName:
                    json.dump(data, envConfig)
                else:
                    envConfig.write(data)   
            envConfig.close()
        home_fs.close()

    def EncyptFile(self,passphrase):
        home=os.environ['HOME']
        gpg = gnupg.GPG(gnupghome=home + '/.gnupg')
        home_fs = open_fs(self.FilePath)
        for path in home_fs.walk.files(filter=['*.gpg']):
		with home_fs.open(path[1:], 'rb') as f:
    			status = gpg.decrypt_file(
				file=f,
				passphrase=passphrase,
				output=self.FilePath + path[:-4]
			)
		print("ok: ", status.ok)
		print("status: ", status.status)
		print("stderr: ", status.stderr)
		f.close()


#test case              
if __name__ == '__main__':
    test=File('/Keys','testjson.txt')
    print(test.ReadFile())
    test.UpdateFile("456")        
        
        


