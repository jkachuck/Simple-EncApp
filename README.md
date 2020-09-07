# Simple-EncApp
This app was created from a base of the Udemy Python 3 class library application. I have made a bunch of modifications. 
I wanted a simple password manager that I knew was keeping my information locally encrypted on the workstation.
I wanted it to to use a standard encyption, which did not require a special app to decrypt.
I wanted to be able to acess the passwords even if the gui was not working.

This requires following libraries:
pyAesCrypt io os sqlite3 tkinter time

There are currently a couple of issues. I will one day get to fixing.
1. The "update" does not work correctly. It can add and delete. 
2. It cant right click and copy.
3. It needs a new function to test if the application is already running. Currently it makes lots of backups to avoid remove a database issue.
4. I want to have a option in the app to state how many backups to keep.
5. A change password script.

I am sure there are more. 

simple_encapp.py - Main GUI application

backend.py - The database part of the main application

decrypt_encapp.py - a command line script decrypt the database

read_decrypted_to_screen.py - a script to read the database to screem




