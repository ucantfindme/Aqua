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

#Student class
class student():
    def __init__(self):
        pass
# Home func
    def refresh(self,h):
        h.destroy()
        student().home()
        pass
    
    def profile(self,name):
        reg=Tk()
        reg.geometry("300x480+940+285")
        reg.maxsize(400,480)
        reg.minsize(400,480)
        reg.title("Register")
        reg.configure(background='purple')

        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Profile",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=150,y=20)
        
        # Frame 2
        f2 = Frame(reg,width=400,height=300,bg='purple')
        f2.place(x=20,y=80)

        l2 = Label(f2,text="Student Id:",fg='lightyellow',bg='purple',anchor='e', font=('roboto',13,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 

        l3 = Label(f2,text="Name:",fg='lightyellow',bg='purple',justify=RIGHT, font=('roboto',13,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=15)

        l4 = Label(f2,text="DOB:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=15) 

        l5 = Label(f2,text="Phone no:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l5.grid(row = 4, column = 0, pady = 10,padx=15) 

        l6 = Label(f2,text="E-Mail:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l6.grid(row = 5, column = 0, pady = 10,padx=15) 

        l7 = Label(f2,text="Batch:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l7.grid(row = 6, column = 0, pady = 10,padx=15) 


    
        l12 = Label(f2,text="Student Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l12.grid(row = 1, column = 1, pady = 10,padx=15) 

        l13 = Label(f2,text="Name:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l13.grid(row = 2, column = 1, pady = 10,padx=15)

        l14 = Label(f2,text="DOB:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l14.grid(row = 3, column = 1, pady = 10,padx=15) 

        l15 = Label(f2,text="Phone no:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l15.grid(row = 4, column = 1, pady = 10,padx=15) 

        l16 = Label(f2,text="E-Mail:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l16.grid(row = 5, column = 1, pady = 10,padx=15) 

        l17 = Label(f2,text="Batch:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l17.grid(row = 6, column = 1, pady = 10,padx=15) 

        reg.mainloop()
    # Welcome frame
    def home(self,name):
        # Home window
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
        pro = Button(f1,text="Profile",bg='orange',relief='flat',underline=0,command=lambda:self.profile(name),font=('roboto',15,'bold'))
        pro.place(x=85,y=40)
        # Login button
        att = Button(f1,text="Attendance",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        att.place(x=85,y=340)

        view = Menubutton(f1,text="View",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        view.menu =  Menu ( view, tearoff = 0, bg='lightblue' ,font=('roboto',13,'normal'))
        view["menu"] =  view.menu
        view.menu.add_command(label="Courses Registered")
        view.menu.add_command(label="Calender")
        view.place(x=85,y=380)
        #close button
        cls = Button(f1,text="Logout",bg='orange',relief='flat',underline=0,command=lambda:lgo(h),font=('roboto',15,'bold'))
        cls.place(x=85,y=500)
        
        # Frame 2
        f2 = Frame(h,width=980,height=130,bg='lightyellow')
        f2.place(x=210,y=10)
        # Heading label
        l2 = Label(f2,text="Welcome "+name,fg='black',bg='lightyellow',font=('roboto',50,'bold'))
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
