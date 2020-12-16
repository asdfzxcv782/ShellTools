import os
import fs
from fs import open_fs
import gnupg
import json

home=os.environ['HOME']

keyDir=home+"/ShellTools/keys"

gpg = gnupg.GPG(gnupghome=home + '/.gnupg')

home_fs = open_fs(keyDir)


def encyptFile():
	for path in home_fs.walk.files(filter=['*.gpg']):
		with home_fs.open(path[1:], 'rb') as f:
    			status = gpg.decrypt_file(
				file=f,
				passphrase=getPassPhrase(),
				output=keyDir + path[:-4]
			)
		print("ok: ", status.ok)
		print("status: ", status.status)
		print("stderr: ", status.stderr)
		f.close()

def getPassPhrase():
	with open_fs(keyDir) as home_fs:
		with home_fs.open('envConfig.json') as passphrase:
			passphrase=json.loads(passphrase.read())
			return passphrase["encrypt"]["passphrase"]
		passphrase.close()
	home_fs.close()		
encyptFile()

