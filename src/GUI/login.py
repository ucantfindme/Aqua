# Impoting tkinter4
import sys
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from GUI.fp import f
from GUI.admin import admin
from GUI.student import student
from GUI.teacher import teacher
#from ...Code.main import login

class l():
    def __init__(self):
        pass
    # Login Submit function  
    def log_submit(self,h,log,name_var,passw_var):
        name=name_var.get()
        password=passw_var.get()
        name_var.set("")
        passw_var.set("")
        s='A' #login(name,password)
        if s=='A':
            h.destroy()
            log.destroy()
            admin().home()
        elif s=='S':
            h.destroy()
            log.destroy()
            student().home()
        elif s=='T':
            h.destroy()
            log.destroy()
            teacher().home()
        else:
            messagebox.showerror("Error", "PLease enter a valid Username or Password")
        pass

    # Login function
    def login(self,h):
        # Login
        log=Tk()
        log.geometry("300x350+940+350")
        log.maxsize(400,350)
        log.minsize(400,350)
        log.title("Login")
        log.configure(background='purple')

        # Frame 1
        f1 = Frame(log,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Login to AMS",bg='purple',fg='lightyellow',font=('verdana',30,'bold'))
        l1.place(x=45,y=30)
        
        # Frame 2
        f2 = Frame(log,width=400,height=300,bg='purple')
        f2.place(x=20,y=140)
        # Label 2 - Email
        l2 = Label(f2,text="E-mail or Id:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 
        # Label 3 - Password
        l3 = Label(f2,text="Password:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=15)
    
        name_var=tk.StringVar()
        passw_var=tk.StringVar()
        # Entry 1 - Email
        e1 = Entry(f2,textvariable=name_var,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 
        # Entry 2 - Password 
        e2 = Entry(f2,textvariable=passw_var, show="*",font=('roboto',12,'normal')) 
        e2.grid(row = 2, column = 1, pady = 10) 

        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=lambda:l().log_submit(h,log,name_var,passw_var),font=('roboto',12,'bold'))
        sub.grid(column=1,row=3,pady="3")

        
        l4 = Button(f2,text="Forgot Password?",fg='lightyellow',bg='purple',relief='flat',command=lambda:f().fp(log), font=('roboto',12,'bold'))
        l4.grid(row = 4, column = 1, pady = 10,padx=15)
        log.mainloop()
