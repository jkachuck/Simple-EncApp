#!/usr/bin/python3

import pyAesCrypt 
import io
import os


encappdata = "simple_encapp.db.aes"

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "test"

#check if the file is there if no encrypted fie is there create one:
if os.path.isfile(encappdata):
    pyAesCrypt.decryptFile(encappdata, "encapp_decrypted.db", password, bufferSize)

else: print ("no file")


# encrypt
#pyAesCrypt.encryptFile("info.txt", "info.txt.aes", password, bufferSize)






