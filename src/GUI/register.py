# Impoting tkinter4
import sys
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
from Classes.Admin import Admin 
# Register class
class r():
    def __init__(self):
        pass
    # Register function
    def sregister(self):
        reg=Tk()
        reg.geometry("300x480+940+285")
        reg.maxsize(400,480)
        reg.minsize(400,480)
        reg.title("Register")
        reg.configure(background='purple')

        def reg_submit():
            studentid=e1.get()
            name=e2.get()
            dob=e3.get()
            ph=e4.get()
            email=e5.get()
            batch=e6.get()
            password=e7.get()
            s=Admin().createStudent(studentid,name,dob,ph,email,batch,password)
            print(s)
            if s:
                messagebox.showinfo("Register", "Registration Successful")
            else:
                messagebox.showerror("Error", "PLease enter valid details")


        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Student Registration",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
        # Frame 2
        f2 = Frame(reg,width=400,height=300,bg='purple')
        f2.place(x=20,y=80)

        l2 = Label(f2,text="Student Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=15) 

        l3 = Label(f2,text="Name:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=15)

        l4 = Label(f2,text="DOB:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=15) 

        l5 = Label(f2,text="Phone no:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l5.grid(row = 4, column = 0, pady = 10,padx=15) 

        l6 = Label(f2,text="E-Mail:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l6.grid(row = 5, column = 0, pady = 10,padx=15) 

        l7 = Label(f2,text="Batch:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l7.grid(row = 6, column = 0, pady = 10,padx=15) 

        l8 = Label(f2,text="Password:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l8.grid(row = 7, column = 0, pady = 10,padx=15)
    
        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 

        e2 = Entry(f2,font=('roboto',12,'normal'))
        e2.grid(row = 2, column = 1, pady = 10) 

        e3 = Entry(f2,font=('roboto',12,'normal'))
        e3.grid(row = 3, column = 1, pady = 10) 

        e4 = Entry(f2,font=('roboto',12,'normal'))
        e4.grid(row = 4, column = 1, pady = 10) 

        e5 = Entry(f2,font=('roboto',12,'normal'))
        e5.grid(row = 5, column = 1, pady = 10) 

        e6 = Entry(f2,font=('roboto',12,'normal'))
        e6.grid(row = 6, column = 1, pady = 10) 
        
        e7 = Entry(f2, show="*",font=('roboto',12,'normal')) 
        e7.grid(row = 7, column = 1, pady = 10) 
        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=reg_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=8,pady="3")

        reg.mainloop()
    
    def tregister(self):
        reg=Tk()
        reg.geometry("300x500+940+270")
        reg.maxsize(400,500)
        reg.minsize(400,500)
        reg.title("Register")
        reg.configure(background='purple')

        def reg_submit():
            teacherid=e1.get()
            name=e2.get()
            dob=e3.get()
            ph=e4.get()
            email=e5.get()
            department=e6.get()
            courses_taught=e7.get()
            password=e8.get()
            s=Admin().createTeacher(name,dob,ph,email,teacherid,department,courses_taught,password)
            print(s)
            if s:
                messagebox.showinfo("Register", "Registration Successful")
            else:
                messagebox.showerror("Error", "PLease enter valid details")


        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Teacher Registration",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
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

        l9 = Label(f2,text="Password:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l9.grid(row = 8, column = 0, pady = 10,padx=10)
    
        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 

        e2 = Entry(f2,font=('roboto',12,'normal'))
        e2.grid(row = 2, column = 1, pady = 10) 

        e3 = Entry(f2,font=('roboto',12,'normal'))
        e3.grid(row = 3, column = 1, pady = 10) 

        e4 = Entry(f2,font=('roboto',12,'normal'))
        e4.grid(row = 4, column = 1, pady = 10) 

        e5 = Entry(f2,font=('roboto',12,'normal'))
        e5.grid(row = 5, column = 1, pady = 10) 

        e6 = Entry(f2,font=('roboto',12,'normal'))
        e6.grid(row = 6, column = 1, pady = 10) 
        
        e7 = Entry(f2,font=('roboto',12,'normal')) 
        e7.grid(row = 7, column = 1, pady = 10) 

        e8 = Entry(f2, show="*",font=('roboto',12,'normal')) 
        e8.grid(row = 8, column = 1, pady = 10) 
        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=reg_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=9,pady="3")

        reg.mainloop()
    
    def courseregister(self):
        reg=Tk()
        reg.geometry("300x390+940+350")
        reg.maxsize(400,390)
        reg.minsize(400,390)
        reg.title("Register")
        reg.configure(background='purple')

        def reg_submit():
            courseid=e1.get()
            title=e2.get()
            prerequisites=e3.get()
            classesenrolled=e4.get()
            facultyassigned=e5.get()
            s=Admin().createStudent(courseid,title,prerequisites,classesenrolled,facultyassigned)
            print(s)
            if s:
                messagebox.showinfo("Register", "Registration Successful")
            else:
                messagebox.showerror("Error", "PLease enter valid details")


        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="Course Registration",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
        # Frame 2
        f2 = Frame(reg,width=400,height=300,bg='purple')
        f2.place(x=20,y=80)

        l2 = Label(f2,text="Course Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=10) 

        l3 = Label(f2,text="Title:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=10)

        l4 = Label(f2,text="Prerequisites:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=10) 

        l5 = Label(f2,text="Class Enrolled:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l5.grid(row = 4, column = 0, pady = 10,padx=10) 

        l6 = Label(f2,text="Faculty Assigned:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l6.grid(row = 5, column = 0, pady = 10,padx=10) 

        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 

        e2 = Entry(f2,font=('roboto',12,'normal'))
        e2.grid(row = 2, column = 1, pady = 10) 

        e3 = Entry(f2,font=('roboto',12,'normal'))
        e3.grid(row = 3, column = 1, pady = 10) 

        e4 = Entry(f2,font=('roboto',12,'normal'))
        e4.grid(row = 4, column = 1, pady = 10) 

        e5 = Entry(f2,font=('roboto',12,'normal'))
        e5.grid(row = 5, column = 1, pady = 10) 

        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=reg_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=6,pady="3")

        reg.mainloop()
    
    def classregister(self):
        reg=Tk()
        reg.geometry("300x350+940+350")
        reg.maxsize(400,350)
        reg.minsize(400,350)
        reg.title("Register")
        reg.configure(background='purple')

        def reg_submit():
            classid=e1.get()
            advisor=e2.get()
            students=e3.get()
            courseenrolled=e4.get()
            s=Admin().createStudent(classid,advisor,students,courseenrolled)
            print(s)
            if s:
                messagebox.showinfo("Register", "Registration Successful")
            else:
                messagebox.showerror("Error", "PLease enter valid details")


        f1 = Frame(reg,width=400,height=100,bg='purple')
        f1.place(x=0,y=0)
        # Label 1
        l1 = Label(f1,text="  Class Registration",bg='purple',fg='lightyellow',font=('verdana',22,'bold'))
        l1.place(x=35,y=20)
        
        # Frame 2
        f2 = Frame(reg,width=400,height=300,bg='purple')
        f2.place(x=20,y=80)

        l2 = Label(f2,text="Class Id:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l2.grid(row = 1, column = 0, pady = 10,padx=10) 

        l3 = Label(f2,text="Advisor:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l3.grid(row = 2, column = 0, pady = 10,padx=10)

        l4 = Label(f2,text="Students:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l4.grid(row = 3, column = 0, pady = 10,padx=10) 

        l5 = Label(f2,text="Courses Enrolled:",fg='lightyellow',bg='purple', font=('roboto',13,'bold'))
        l5.grid(row = 4, column = 0, pady = 10,padx=10) 
    
        # Entry 1 - Email
        e1 = Entry(f2,font=('roboto',12,'normal'))
        e1.grid(row = 1, column = 1, pady = 10) 

        e2 = Entry(f2,font=('roboto',12,'normal'))
        e2.grid(row = 2, column = 1, pady = 10) 

        e3 = Entry(f2,font=('roboto',12,'normal'))
        e3.grid(row = 3, column = 1, pady = 10) 

        e4 = Entry(f2,font=('roboto',12,'normal'))
        e4.grid(row = 4, column = 1, pady = 10) 

        # Submit button
        sub = Button(f2,text="Submit",bg='orange',command=reg_submit,font=('roboto',12,'bold'))
        sub.grid(column=1,row=5,pady="3")

        reg.mainloop()
        pass
