import sqlite3
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def login(userid,password):
    #edit the path of folder DB accordingly
    path=os.path.abspath('.')
    #print(path+'/src/DB/login.db')
    conn = sqlite3.connect(path+'/src/DB/login.db')
    cursor = conn.cursor()
    lst=cursor.execute('''SELECT * FROM LOGS WHERE USERNAME=? AND PASS=?''',(userid,password))
    data=""
    for i in lst:
        data=i
    conn.commit()
    conn.close()
    if not data:
        print("Incorrect Password")
        #pop-up a dialogue box 
        return 'F'
    #login successfull pop-up message
    if data[2]=='A':
        print("Welcome Admin,",data[0])
        #Open Admin Window
    elif data[2]=='S':
        print("Welcome Student,",data[0])
        #Open Student Window
    else:
        print("Welcome Teacher,",data[0])
        #Open Teacher Window
    #return respective object
    return data[2] 
def forgotPassword(userid,otp):
    if otp!="19347":
        #pop-up wrong otp dialogue box
        return False
    return True
def updatepass(userid,newpass):
    path=os.path.abspath('.')
    conn = sqlite3.connect(path+'/src/DB/login.db')
    cursor = conn.cursor()
    lst=cursor.execute('''SELECT * FROM LOGS WHERE USERNAME=?''',(userid,))
    if not lst:
        #pop-up username doesn't exist
        return False    
    val=cursor.execute('''UPDATE LOGS SET PASS=? WHERE USERNAME=?''',(newpass,userid))
    print("Password Updated")
    conn.commit()
    conn.close()
    return True
def logout(h):
    x=messagebox.askquestion("Logout", "Are you sure?")
    print(x)
    if x=="yes": h.destroy()
    #return to default window with no user logged in
    pass
"""login("Admin347","marinpappa")
login("NaSaPaKri","mikupappa")
login("NSPKrishna","Maipappa")
login("NSPKrishna","maipappa")
forgotPassword("NSPKrishna",19347)
login("NSPKrishna","Maipappa")
login("NSPKrishna","maipappa")"""