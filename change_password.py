#!/usr/bin/python3

import pyAesCrypt 
import io
import os


encappdata = "simple_encapp.db.aes"
decrypted = "encapp_decrypted.db"


# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
#password = "test"
#newpassword = "test2"


while True:
	password = input("Enter your old password: ") 
	if os.path.isfile(encappdata):
		try: pyAesCrypt.decryptFile(encappdata, decrypted, password, bufferSize)
		except ValueError: print ("Wrong old password" + "\n" )
		if os.path.isfile(decrypted):
			newpassword = input("Enter your new password: ")
			pyAesCrypt.encryptFile( decrypted, encappdata, newpassword, bufferSize)
			os.remove(decrypted)
			break
	else: print ("No file" + "\n")
	

