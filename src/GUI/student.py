# Impoting tkinter4
import sys
import os
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo
#from home import welcome

class student():
    def __init__(self):
        pass

    def refresh(self,h):
        h.destroy()
        student().home()
        pass

    # welcome frame
    def home(self):
        # home
        h=Tk()
        h.title("AMS Student")
        h.configure(background='purple')
        h.geometry("1200x700+170+80")
        h.maxsize(1200,700)
        h.minsize(1200,700)
        
        # Frame 1
        f1 = Frame(h,width=190,height=680,bg='orange')
        f1.place(x=10,y=10)
        # Home button
        hom = Button(f1,text="Profile",bg='orange',relief='flat',underline=0,font=('roboto',12,'bold'))
        hom.place(x=90,y=40)
        # Login button
        log = Button(f1,text="Login",bg='orange',relief='flat',underline=0,font=('roboto',12,'bold'))
        log.place(x=90,y=340)
        # Registration button
        reg = Button(f1,text="Register",bg='orange',relief='flat',underline=0,font=('roboto',12,'bold'))
        reg.place(x=90,y=380)
        #close button
        cls = Button(f1,text="Logout",bg='orange',relief='flat',underline=0,command=lambda:lgo(h),font=('roboto',12,'bold'))
        cls.place(x=90,y=500)
        
        # Frame 2
        f2 = Frame(h,width=980,height=130,bg='lightyellow')
        f2.place(x=210,y=10)
        # Heading label
        l2 = Label(f2,text="Welcome to AMS",fg='black',bg='lightyellow',font=('roboto',50,'bold'))
        l2.place(x=220,y=35)
        
        # Frame 3
        f3 = Frame(h,width=980,height=530,bg='lightblue')
        f3.place(x=210,y=160)
        path=os.path.abspath('.')+"/src/GUI/Aqua.png"
        img=Image.open(path)
        img = img.resize((980, 530), Image. ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = tk.Label(f3, image = img)
        label.place(x=0,y=0)
        h.mainloop()