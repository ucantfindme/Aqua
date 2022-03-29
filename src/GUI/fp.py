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
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo


class f():
    def __init__(self):
        pass
    # Forgot Password Submit function  
    def fp_submit(self,fp,name_var,pin_var):
        name=name_var.get()
        pin=pin_var.get()
        name_var.set("")
        pin_var.set("")
        if forpass(name,pin):
            fp.destroy()
            #home()
        else:
            messagebox.showerror("Error", "PLease enter a valid Username and Pin")
        pass

    #Forgot password
    def fp(self,log):
        log.destroy()
        fp=Tk()
        fp.geometry("300x350+580+210")
        fp.maxsize(400,350)
        fp.minsize(400,350)
        fp.title("Login")
        fp.configure(background='purple')

        # Frame 1
        f1 = Frame(fp,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Login to AMS",bg='purple',fg='black',font=('verdana',30,'bold'))
        l1.place(x=45,y=30)
        
        # Frame 2
        f2 = Frame(fp,width=400,height=300,bg='purple')
        f2.place(x=20,y=140)
        # Label 2 - Email
        l2 = Label(f2,text="E-mail or Id:",bg='purple', font=('roboto',15,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 
        # Label 3 - Pin
        l3 = Label(f2,text="Pin:",bg='purple', font=('roboto',15,'bold'))
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
        sub = Button(f2,text="Submit",bg='orange',command=lambda:self.fp_submit(fp,name_var,pin_var),font=('roboto',12,'bold'))
        sub.grid(column=1,row=3,pady="3")
        fp.mainloop()
