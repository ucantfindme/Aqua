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
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo


class l():
    def __init__(self):
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
        
        # Submit func
        def log_submit():
            name=e1.get()
            password=e2.get()
            print(name,password)
            s=logfun(name,password)
            print(s)
            if s=='A':
                h.destroy()
                log.destroy()
                admin().home(name)
            elif s=='S':
                h.destroy()
                log.destroy()
                student().home(name)
            elif s=='T':
                h.destroy()
                log.destroy()
                teacher().home(name)
            else:
                messagebox.showerror("Error", "PLease enter a valid Username or Password")

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
    
        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 
        # Entry 2 - Password 
        e2 = Entry(f2, show="*",font=('roboto',12,'normal')) 
        e2.grid(row = 2, column = 1, pady = 10) 
        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=log_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=3,pady="3")
        #forgot password button
        l4 = Button(f2,text="Forgot Password?",fg='lightyellow',bg='purple',relief='flat',command=lambda:f().fp(log,h), font=('roboto',12,'bold'))
        l4.grid(row = 4, column = 1, pady = 10,padx=15)
        log.mainloop()
