#!/usr/bin/python3

import pyAesCrypt 
import io
import os
from tkinter import *
import tkinter.simpledialog
#from tkinter import simpledialog
#import backend
import time

#I am adding the decrypt before anything happens.
bufferSize = 64 * 1024
#setting a default password so there is something is nothing is entered
password = "test"

#moved window creation to top from only one tk
window=Tk()

#setting the location of the db
decrypted_loc = "./simple_encapp.db"

# adding a check for file
testNew = os.path.isfile(decrypted_loc)
print(testNew)
if testNew == True:
    fileSizeTest = os.stat(decrypted_loc).st_size
    print(fileSizeTest)
    if fileSizeTest > 8192:
        makeSureTest=tkinter.simpledialog.askstring("Cleanup Check", "If you dont want to exit type GO")
        if makeSureTest != "GO":
            quit()
    newFileTest=tkinter.simpledialog.askstring("Running Check", "if new enter NEW")
    if newFileTest != "NEW":
        quit()   



def getpassword():
    password = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
    #print(password)
    return password


if os.path.isfile( decrypted_loc + ".aes"):
    while True:
        try:
            #print("decrypt")
            password = getpassword()
            pyAesCrypt.decryptFile(decrypted_loc + ".aes", decrypted_loc, password, bufferSize)
            break
        except ValueError:
            print("Wrong Password Try Again")

else: password = getpassword()                        

#moving the import of backend
import backend
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #print(selected_tuple)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_limit_command():
    list1.delete(0,END)
    for row in backend.view_limit():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(website_text.get(),webid_text.get(),year_text.get(),webpasswd_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(website_text.get(),webid_text.get(),year_text.get(),webpasswd_text.get())
    list1.insert(END,(website_text.get(),webid_text.get(),year_text.get(),webpasswd_text.get()))
    list1.delete(0,END)
    search_command()
    #added backup when you add a new password:
    pyAesCrypt.encryptFile(decrypted_loc, decrypted_loc + "." + time.strftime("%Y%m%d-%H%M%S") + ".aes", password, bufferSize)


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],website_text.get(),webid_text.get(),year_text.get(),webpasswd_text.get())

def close_command():
    pyAesCrypt.encryptFile(decrypted_loc, decrypted_loc + ".aes", password, bufferSize)
    #print("encrypt")
    os.remove(decrypted_loc)
    window.quit()


window.wm_title("Simple EncApp")


l1=Label(window,text="Web Site")
l1.grid(row=0,column=0)

l2=Label(window,text="User ID")
l2.grid(row=0,column=2)

l3=Label(window,text="Date")
l3.grid(row=1,column=0)

l4=Label(window,text="Password")
l4.grid(row=1,column=2)

website_text=StringVar()
e1=Entry(window,textvariable=website_text)
e1.grid(row=0,column=1)

webid_text=StringVar()
e2=Entry(window,textvariable=webid_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

webpasswd_text=StringVar()
e4=Entry(window,textvariable=webpasswd_text)
e4.grid(row=1,column=3)
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0, rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#sb1.pack( side = RIGHT, fill = Y)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1=Button(window,text="View All", width=12,command=view_limit_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=close_command)
b6.grid(row=7,column=3)

window.protocol("WM_DELETE_WINDOW", close_command)



window.mainloop()
