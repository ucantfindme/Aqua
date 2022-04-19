# Impoting tkinter4
import os
import sys
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo


# Teacher class
class teacher():
    def __init__(self):
        pass

    # Home func
    def refresh(self,h):
        h.destroy()
        self.home()
        pass
    
    def profile(self,name):
        reg=Tk()
        reg.geometry("300x42+940+315")
        reg.maxsize(400,420)
        reg.minsize(400,420)
        reg.title("Profile")
        reg.configure(background='purple')

        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Profile",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=150,y=20)
        
        # Frame 2
        f2 = Frame(reg,width=400,height=300,bg='purple')
        f2.place(x=20,y=80)

        l2 = Label(f2,text="Teacher Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=10) 

        l3 = Label(f2,text="Name:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=10)

        l4 = Label(f2,text="DOB:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=10) 

        l5 = Label(f2,text="Phone no:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l5.grid(row = 4, column = 0, pady = 10,padx=10) 

        l6 = Label(f2,text="E-Mail:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l6.grid(row = 5, column = 0, pady = 10,padx=10) 

        l7 = Label(f2,text="Department:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l7.grid(row = 6, column = 0, pady = 10,padx=10) 

        l8 = Label(f2,text="Courses Taught:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l8.grid(row = 7, column = 0, pady = 10,padx=10) 

    
        
        l12 = Label(f2,text="Teacher Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l12.grid(row = 1, column = 1, pady = 10,padx=10) 

        l13 = Label(f2,text="Name:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l13.grid(row = 2, column = 1, pady = 10,padx=10)

        l14 = Label(f2,text="DOB:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l14.grid(row = 3, column = 1, pady = 10,padx=10) 

        l15 = Label(f2,text="Phone no:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l15.grid(row = 4, column = 1, pady = 10,padx=10) 

        l16 = Label(f2,text="E-Mail:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l16.grid(row = 5, column = 1, pady = 10,padx=10) 

        l17 = Label(f2,text="Department:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l17.grid(row = 6, column = 1, pady = 10,padx=10) 

        l18 = Label(f2,text="Courses Taught:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l18.grid(row = 7, column = 1, pady = 10,padx=10) 

        reg.mainloop()

    def upload(self,h):
        u=Toplevel(h)
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("File Uplaod")
        u.configure(background='purple')

        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("Csv files",
                                                                "*.csv*"),
                                                            ("all files",
                                                                "*.*")))
            if filename is not None:
                messagebox.showinfo("Upload", "Upload Successful")
                u.destroy()
            else:
                messagebox.showerror("Error", "PLease choose a file.")

        
        f1 = Frame(u,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Upload Attendance",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
        # Frame 2
        f2 = Frame(u,width=400,height=300,bg='purple')
        f2.place(x=0,y=80)

        l2 = Label(f2,text="",fg='lightyellow',bg='purple', font=('roboto',10,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=10) 

        sub = Button(f2,text="Choose",bg='orange',command=browseFiles,font=('roboto',12,'bold'))
        sub.grid(column=0,row=2,pady="3",padx=150)

        u.mainloop()
    # Welcome frame
    def home(self,name):
        # Home window
        h=Tk()
        h.title("AMS Teacher")
        h.configure(background='purple')
        h.geometry("1200x700+170+80")
        h.maxsize(1200,700)
        h.minsize(1200,700)
        
        # Frame 1
        f1 = Frame(h,width=190,height=680,bg='orange')
        f1.place(x=10,y=10)
        # Home button
        pro = Button(f1,text="Profile",bg='orange',relief='flat',underline=0,command=lambda:self.profile(name),font=('roboto',15,'bold'))
        pro.place(x=2,y=40)
        # View button
        view = Menubutton(f1,text="View",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        view.menu =  Menu ( view, tearoff = 0, bg='lightblue' ,font=('roboto',13,'normal'))
        view["menu"] =  view.menu
        view.menu.add_command(label="Sheduled Meetings")
        view.menu.add_command(label="Meeting Attendance")
        view.menu.add_command(label="Overall Attendance")
        view.place(x=2,y=300)
        # Registration button
        sm = Button(f1,text="Shedule Meeting",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        sm.place(x=2,y=340)
        # Registration button
        sm = Button(f1,text="Upload Attendance",bg='orange',relief='flat',underline=0,command=lambda:self.upload(h),font=('roboto',15,'bold'))
        sm.place(x=2,y=380)
        #close button
        cls = Button(f1,text="Logout",bg='orange',relief='flat',underline=0,command=lambda:lgo(h),font=('roboto',15,'bold'))
        cls.place(x=2,y=500)
        
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
