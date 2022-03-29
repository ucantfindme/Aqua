# Impoting tkinter4
import sys
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from GUI.student import student
from GUI.teacher import teacher
from GUI.admin import admin
<<<<<<< HEAD
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo,updatepass as up
#from ...Code.main import forgotPassword
=======
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo

>>>>>>> 843de92ce5514d4daa8c1b647d19595691843192

class f():
    def __init__(self):
        pass

    def confirm(self,h):
        c=Tk()
        c.geometry("300x350+940+350")
        c.maxsize(400,350)
        c.minsize(400,350)
        c.title("Update")
        c.configure(background='purple')
        def c_submit(c,h):
            name=e1.get()
            newpass=e2.get()
            cpass=e3.get()
            print(name,newpass)
            if newpass!=cpass:
                messagebox.showerror("Error", "New Password and Confirm Password are not same")
            else:
                if up(name,newpass):
                    c.destroy()
        # Frame 1
        f1 = Frame(c,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Update Password",fg='lightyellow',bg='purple',font=('verdana',25,'bold'))
        l1.place(x=40,y=30)
        
        # Frame 2
        f2 = Frame(c,width=400,height=300,bg='purple')
        f2.place(x=20,y=120)
        # Label 2 - Email
        l2 = Label(f2,text="E-mail or Id:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 
        # Label 3 - New password
        l3 = Label(f2,text="New Password:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=15)
        # Label 4 - New password
        l4 = Label(f2,text="Confirm:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=15)

        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 
        # Entry 2 - New password
        e2 = Entry(f2, font=('roboto',12,'normal')) 
        e2.grid(row = 2, column = 1, pady = 10) 
        # Entry 2 - Confirm password 
        e3 = Entry(f2, font=('roboto',12,'normal')) 
        e3.grid(row = 3, column = 1, pady = 10)

        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=lambda:c_submit(c,h),font=('roboto',12,'bold'))
        sub.grid(column=1,row=4,pady="3")
        c.mainloop() 

    #Forgot password
    def fp(self,log,h):
        log.destroy()
        fp=Tk()
        fp.geometry("300x350+940+350")
        fp.maxsize(400,350)
        fp.minsize(400,350)
        fp.title("Forgot Password")
        fp.configure(background='purple')
        
        def fp_submit(fp,h):
            name=e1.get()
            pin=e2.get()
            print(name,pin)
            if forpass(name,pin):
                fp.destroy()
                self.confirm(h)
            else:
                messagebox.showerror("Error", "PLease enter a valid Username or Pin")
        # Frame 1
        f1 = Frame(fp,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Forgot Password",fg='lightyellow',bg='purple',font=('verdana',25,'bold'))
        l1.place(x=40,y=30)
        
        # Frame 2
        f2 = Frame(fp,width=400,height=300,bg='purple')
        f2.place(x=20,y=140)
        # Label 2 - Email
        l2 = Label(f2,text="E-mail or Id:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 
        # Label 3 - Pin
        l3 = Label(f2,text="Pin:",fg='lightyellow',bg='purple', font=('roboto',15,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=15)
    
        name_var=tk.StringVar()
        pin_var=tk.StringVar()
        # Entry 1 - Email
        e1 = Entry(f2,textvariable=name_var,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 
        # Entry 2 - Pin 
        e2 = Entry(f2,textvariable=pin_var, font=('roboto',12,'normal')) 
        e2.grid(row = 2, column = 1, pady = 10) 

        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=lambda:fp_submit(fp,h),font=('roboto',12,'bold'))
        sub.grid(column=1,row=3,pady="3")
        fp.mainloop()
