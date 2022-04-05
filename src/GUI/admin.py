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
from GUI.register import r
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo


class admin():
    def __init__(self):
        pass
#go back to the home page

    def refresh(self,h):
        h.destroy()
        admin().home()
        pass
    #Welcome Home
    #Home window
    def home(self):
        # home
        h=Tk()
        h.title("AMS Admin")
        h.configure(background='purple')
        h.geometry("1200x700+170+80")
        h.maxsize(1200,700)
        h.minsize(1200,700)
        
        # Frame 1
        f1 = Frame(h,width=190,height=680,bg='orange')
        f1.place(x=10,y=10)

        # Logout button
        reg = Button(f1,text="Home",bg='orange',relief='flat',underline=0,command=lambda:self.refresh(h),font=('roboto',15,'bold'))
        reg.place(x=85,y=40)

        # View button
        view = Menubutton(f1,text="View",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        view.menu =  Menu ( view, tearoff = 0, bg='lightblue' ,font=('roboto',13,'normal'))
        view["menu"] =  view.menu
        view.menu.add_command(label="Student registration")
        view.menu.add_command(label="Teacher registration")
        view.menu.add_command(label="Class registration")
        view.menu.add_command(label="Course registration")
        view.place(x=85,y=340)

        # Create button
        create = Menubutton(f1,text="Create",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        create.menu =  Menu ( create, tearoff = 0, bg='lightblue' ,font=('roboto',13,'normal'))
        create["menu"] =  create.menu
        create.menu.add_command(label="Student",command=lambda:r().sregister())
        create.menu.add_command(label="Teacher",command=lambda:r().tregister())
        create.menu.add_command(label="Class",command=lambda:r().classregister())
        create.menu.add_command(label="Course",command=lambda:r().courseregister())
        create.place(x=85,y=380)

        #close button
        cls = Button(f1,text="Logout",bg='orange',relief='flat',underline=0,command=lambda:lgo(h),font=('roboto',15,'bold'))
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
        # Loading image
        path=os.path.abspath('.')+"/src/GUI/Aqua.png"
        img=Image.open(path)
        img = img.resize((980, 530), Image. ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = tk.Label(f3, image = img)
        label.place(x=0,y=0)
        h.mainloop()
