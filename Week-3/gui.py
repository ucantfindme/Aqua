# Impoting tkinter
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog

def home():
    h.title("AMS")
    h.configure(background='purple')
    h.geometry("1200x700")
    h.maxsize(1200,700)
    h.minsize(1200,700)
    
    f1 = Frame(h,width=190,height=680,bg='orange')
    f1.place(x=10,y=10)
    hom = Button(f1,text="Home",bg='orange',relief='flat',underline=0,command=home,font=('roboto',12,'bold'))
    hom.place(x=90,y=40)
    log = Button(f1,text="Login",bg='orange',relief='flat',underline=0,command=login,font=('roboto',12,'bold'))
    log.place(x=90,y=340)
    reg = Button(f1,text="Register",bg='orange',relief='flat',underline=0,command=register,font=('roboto',12,'bold'))
    reg.place(x=90,y=380)
    cls = Button(f1,text="Close",bg='orange',relief='flat',underline=0,command=h.destroy,font=('roboto',12,'bold'))
    cls.place(x=90,y=500)
    
    f2 = Frame(h,width=980,height=130,bg='lightyellow')
    f2.place(x=210,y=10)
    l2 = Label(f2,text="Welcome to AMS",bg='lightyellow',font=('roboto',50,'bold'))
    l2.place(x=220,y=35)
    
    f3 = Frame(h,width=980,height=530,bg='lightblue')
    f3.place(x=210,y=160)
    
def sub():
    """
    name=name_var.get()
    password=passw_var.get()
    name_var.set("")
    passw_var.set("")
    welcome.destroy()
    home()
    """
    pass
def login():
    
    welcome=Tk()
    welcome.geometry("300x350")
    welcome.maxsize(400,350)
    welcome.minsize(400,350)
    welcome.title("Login")
    welcome.configure(background='purple')

    f1 = Frame(welcome,width=400,height=100,bg='purple')
    f1.place(x=0,y=0)
    l1 = Label(f1,text="Login to AMS",bg='purple',fg='black',font=('verdana',30,'bold'))
    l1.place(x=45,y=30)
    
    f2 = Frame(welcome,width=400,height=300,bg='purple')
    f2.place(x=20,y=140)
    l2 = Label(f2,text="E-mail or Id:",bg='purple', font=('roboto',15,'bold'))
    l3 = Label(f2,text="Password:",bg='purple', font=('roboto',15,'bold'))
    l2.grid(row = 1, column = 0, pady = 10,padx=15) 
    l3.grid(row = 2, column = 0, pady = 10,padx=15)

    e1 = Entry(f2,textvariable=name_var,font=('roboto',12,'normal')) 
    e2 = Entry(f2,textvariable=passw_var, show="*",font=('roboto',12,'normal')) 
    e1.grid(row = 1, column = 1, pady = 10) 
    e2.grid(row = 2, column = 1, pady = 10) 
    submit = Button(f2,text="Submit",bg='orange',command=welcome.destroy,font=('roboto',12,'bold'))
    submit.grid(column=1,row=3,pady="3")
    welcome.mainloop()

def register():
    pass

if __name__ == "__main__":
    h=Tk()
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    home()
