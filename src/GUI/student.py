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
from Classes.Student import Student
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
    def attendance(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')

        def u_submit():
            id = e1.get()
            ret=Student().getAttendance(id)
            print(ret)
            if ret is not None:
                u.destroy()
            else:
                messagebox.showerror("Error", "Please enter valid details.")

        
        f1 = Frame(u,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="  View Attendance",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
        # Frame 2
        f2 = Frame(u,width=400,height=300,bg='purple')
        f2.place(x=0,y=80)

        l2 = Label(f2,text="Course ID",fg='lightyellow',bg='purple', font=('roboto',12,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=10) 

        e1= Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 

        sub = Button(f2,text="Submit",bg='orange',command=u_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=2,pady="3",padx=40)

        u.mainloop()

    #profile func
    def profile(self,name):
        reg=Tk()
        reg.geometry("300x420+940+315")
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

        ret=Student().viewProfile()
        
        l12 = Label(f2,text=ret[0],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l12.grid(row = 1, column = 1, pady = 10,padx=10) 

        l13 = Label(f2,text=ret[2],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l13.grid(row = 2, column = 1, pady = 10,padx=10)

        l14 = Label(f2,text=ret[3],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l14.grid(row = 3, column = 1, pady = 10,padx=10) 

        l15 = Label(f2,text=ret[4],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l15.grid(row = 4, column = 1, pady = 10,padx=10) 

        l16 = Label(f2,text=ret[5],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l16.grid(row = 5, column = 1, pady = 10,padx=10)  

        l17 = Label(f2,text=ret[6],fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l17.grid(row = 6, column = 1, pady = 10,padx=15) 

        reg.mainloop()
    
    def viewRegisteredCourses(self):
        u=Toplevel()
        u.geometry("300x200+940+445")
        u.maxsize(400,480)
        u.minsize(400,200)
        u.title("View")
        u.configure(background='purple')
        ret=Student().viewRegisteredCourses()
        print(ret)
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
        treev.column("1", width = 90, anchor ='c')
        treev.column("2", width = 90, anchor ='sw')
        treev.column("3", width = 100, anchor ='sw')
        treev.column("4", width = 100, anchor ='sw')
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text ="Course Id")
        treev.heading("2", text ="Title")
        treev.heading("3", text ="Batch")
        treev.heading("4", text ="Faculty")
        
        # Inserting the items and their features to the columns built
        for i in ret:
            treev.insert("", 'end', text ="L1",values =(i[0],i[1],i[3],i[4]))
        u.mainloop()
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
        pro.place(x=4,y=40)
        # Login button
        att = Button(f1,text="Attendance",bg='orange',relief='flat',underline=0,command=self.attendance,font=('roboto',15,'bold'))
        att.place(x=4,y=340)
        #view button
        view  = Button(f1,text="Courses Registered",bg='orange',relief='flat',underline=0,command=self.viewRegisteredCourses,font=('roboto',15,'bold'))
        view.place(x=4,y=380)
        #close button
        cls = Button(f1,text="Logout",bg='orange',relief='flat',underline=0,command=lambda:lgo(h),font=('roboto',15,'bold'))
        cls.place(x=4,y=500)
        
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
