# Impoting tkinter4
import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from GUI.register import r
from Classes.Admin import Admin
from Classes.Welcome import login as logfun, forgotPassword as forpass, logout as lgo


class admin():
    def __init__(self):
        pass
#go back to the home page

    def refresh(self,h,name):
        h.destroy()
        admin().home(name)
        pass
    def viewStudentRegistrations(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')
        ret=Admin().viewStudentRegistrations()
        treev = ttk.Treeview(u, selectmode ='browse')
        
        # Calling pack method w.r.to treeview
        treev.pack(side ='left')
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(u, orient ="vertical", command = treev.yview)
        
        # Calling pack method w.r.to vertical
        # scrollbar
        verscrlbar.pack(side ='left', fill ='x')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3")
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 120, anchor ='c')
        treev.column("2", width = 130, anchor ='sw')
        treev.column("3", width = 130, anchor ='sw')
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text ="Student Id")
        treev.heading("2", text ="Name")
        treev.heading("3", text ="Batch")
        
        # Inserting the items and their features to the columns built
        for i in ret:
            treev.insert("", 'end', text ="L1",values =(i[0],i[1],i[2]))
        u.mainloop()
        
    def viewTeacherRegistrations(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')
        ret=Admin().viewTeacherRegistrations()
        
        treev = ttk.Treeview(u, selectmode ='browse')
        
        # Calling pack method w.r.to treeview
        treev.pack(side ='left')
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(u, orient ="vertical", command = treev.yview)
        
        # Calling pack method w.r.to vertical
        # scrollbar
        verscrlbar.pack(side ='left', fill ='x')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3","4")
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 90, anchor ='c')
        treev.column("2", width = 90, anchor ='sw')
        treev.column("3", width = 100, anchor ='sw')
        treev.column("4", width = 100, anchor ='sw')
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text ="Teacher Id")
        treev.heading("2", text ="Name")
        treev.heading("3", text ="Dept")
        treev.heading("4", text ="Courses")
        
        # Inserting the items and their features to the columns built
        for i in ret:
            treev.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3]))
        u.mainloop()
    
    def viewCourseRegistrations(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')
        ret=Admin().viewCourseRegistrations()
        
        treev = ttk.Treeview(u, selectmode ='browse')
        
        # Calling pack method w.r.to treeview
        treev.pack(side ='left')
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(u, orient ="vertical", command = treev.yview)
        
        # Calling pack method w.r.to vertical
        # scrollbar
        verscrlbar.pack(side ='left', fill ='x')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3", "4")
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 70, anchor ='c')
        treev.column("2", width = 130, anchor ='sw')
        treev.column("3", width = 90, anchor ='sw')
        treev.column("4", width = 90, anchor ='sw')
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text ="Course Id")
        treev.heading("2", text ="Title")
        treev.heading("3", text ="Batchs")
        treev.heading("4", text ="Faculty")
        
        # Inserting the items and their features to the columns built
        for i in ret:
            treev.insert("", 'end', text ="L1",values =(i[0],i[1],i[3],i[4]))
        u.mainloop()
        
    def viewClassRegistrations(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')
        ret=Admin().viewClassRegistrations()
        
        treev = ttk.Treeview(u, selectmode ='browse')
        
        # Calling pack method w.r.to treeview
        treev.pack(side ='left')
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(u, orient ="vertical", command = treev.yview)
        
        # Calling pack method w.r.to vertical
        # scrollbar
        verscrlbar.pack(side ='left', fill ='x')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3", "4")
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 70, anchor ='c')
        treev.column("2", width = 90, anchor ='sw')
        treev.column("3", width = 110, anchor ='sw')
        treev.column("4", width = 110, anchor ='sw')
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text ="Class Id")
        treev.heading("2", text ="Advisor")
        treev.heading("3", text ="Students")
        treev.heading("4", text ="Courses")
        
        # Inserting the items and their features to the columns built
        for i in ret:
            treev.insert("", 'end', text ="L1",values =(i[0],i[1],i[2],i[3]))
        u.mainloop()
    
    #Welcome Home
    #Home window
    def home(self,name):
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
        reg = Button(f1,text="Home",bg='orange',relief='flat',underline=0,command=lambda:self.refresh(h,name),font=('roboto',15,'bold'))
        reg.place(x=85,y=40)

        # View button
        view = Menubutton(f1,text="View",bg='orange',relief='flat',underline=0,font=('roboto',15,'bold'))
        view.menu =  Menu ( view, tearoff = 0, bg='lightblue' ,font=('roboto',13,'normal'))
        view["menu"] =  view.menu
        view.menu.add_command(label="Student registration",command=self.viewStudentRegistrations)
        view.menu.add_command(label="Teacher registration",command=self.viewTeacherRegistrations)
        view.menu.add_command(label="Class registration",command=self.viewClassRegistrations)
        view.menu.add_command(label="Course registration",command=self.viewCourseRegistrations)
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
