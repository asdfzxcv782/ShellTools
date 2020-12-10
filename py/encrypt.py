import os
import fs
from fs import open_fs
import gnupg

keyDir="../keys"

gpg = gnupg.GPG(gnupghome='/home/ushow/.gnupg')

home_fs = open_fs(keyDir)


def encyptFile():
	for path in home_fs.walk.files(filter=['*.gpg']):
		with home_fs.open(path[1:], 'rb') as f:
    			status = gpg.decrypt_file(
				file=f,
				passphrase='vshow2351700',
				output=keyDir + path[:-4]
			)
		print("ok: ", status.ok)
		print("status: ", status.status)
		print("stderr: ", status.stderr)

encyptFile()
'''
for path in home_fs.walk.files(filter=['*.gpg']):
	print(home_fs)
	print(keyDir + path[:-4])
'''
