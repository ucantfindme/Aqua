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
from GUI.login import l

# Welcome class
class welcome():
    def __init__(self):
        print("")
        pass

# Home func    
    def refresh(self,h):
        h.destroy()
        welcome().home()
        pass

    # Welcome frame
    def home(self):
        # home window
        h=Tk()
        h.title("AMS")
        h.configure(background='purple')
        h.geometry("1200x700+170+80")
        h.maxsize(1200,700)
        h.minsize(1200,700)
        
        # Frame 1
        f1 = Frame(h,width=190,height=680,bg='orange')
        f1.place(x=10,y=10)
        # Home button
        hom = Button(f1,text="Home",bg='orange',relief='flat',underline=0,command=lambda:self.refresh(h),font=('roboto',15,'bold'))
        hom.place(x=85,y=40)
        # Login button
        log = Button(f1,text="Login",bg='orange',relief='flat',underline=0,command=lambda:l().login(h),font=('roboto',15,'bold'))
        log.place(x=85,y=460)
        #close button
        cls = Button(f1,text="Close",bg='orange',relief='flat',underline=0,command=lambda:h.destroy(),font=('roboto',15,'bold'))
        cls.place(x=85,y=500)
        
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
