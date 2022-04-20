
from Classes import Person, Student, Teacher, Class, Course
import sqlite3
import os
class Admin(Person.Person):
    def __init__(self,adminid="Admin347",name="Pavan",dob="12-06-2000",ph="12345",email="abc@gmail.com",type='A'):
        super().__init__(adminid,name,dob,ph,email,type)
        self.adminid=adminid
        
    def createStudent(self,studentid,name,dob,ph,email,batch,password):
        stu=Student.Student(studentid,name,dob,ph,email,batch,password)
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO PERSON VALUES (?,?,?,?,?,'S')''',(studentid,name,dob,ph,email))
        cursor.execute('''INSERT INTO STUDENT VALUES (?,?,?)''',(studentid,name,batch))
        # Display data inserted
        """print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM PERSON''')
        for row in data:
            print(row)"""
        #Commit your changes in the database	
        conn.commit()
        #Closing the connection
        conn.close()
        
        conn = sqlite3.connect(path+'/login.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO LOGS VALUES (?,?,?)''',(studentid,password,'S'))
        conn.commit()
        conn.close()
        
        return stu
    
    def createTeacher(self,name,dob,ph,email,teacherId,department,courses_taught,password):
        tea=Teacher.Teacher(name,dob,ph,email,teacherId,department,courses_taught,password)
        #Add new column to Teacher Table in DB
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO PERSON VALUES (?,?,?,?,?,'S')''',(teacherId,name,dob,ph,email))
        cursor.execute('''INSERT INTO TEACHER VALUES (?,?,?)''',(teacherId,name,department,courses_taught))
        # Display data inserted
        """print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM PERSON''')
        for row in data:
            print(row)"""
        #Commit your changes in the database	
        conn.commit()
        #Closing the connection
        conn.close()
        
        conn = sqlite3.connect(path+'/login.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO LOGS VALUES (?,?,?)''',(teacherId,password,'T'))
        conn.commit()
        conn.close()
        
        return tea
    
    def createClass(self,ClassId,Advisor,Students,CoursesEnrolled):
        cla=Class.Class(ClassId,Advisor,Students,CoursesEnrolled)
        #Add new column to Class Table in DB
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO CLASS VALUES (?,?,?,?)''',(ClassId,Advisor,Students,CoursesEnrolled))
        # Display data inserted
        """print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM PERSON''')
        for row in data:
            print(row)"""
        #Commit your changes in the database	
        conn.commit()
        #Closing the connection
        conn.close()
        return cla
    
    def createCourse(self,CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned):
        cou=Course.Course(CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,[])
        #Add new column to Course Table in DB
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO COURSE VALUES (?,?,?,?,?,'')''',(CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned))
        # Display data inserted
        """print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM PERSON''')
        for row in data:
            print(row)"""
        #Commit your changes in the database	
        conn.commit()
        #Closing the connection
        conn.close()
        return cou
    
    def viewStudentRegistrations(self):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM STUDENT''')
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret
        
    def viewTeacherRegistrations(self):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM TEACHER''')
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret
    
    def viewCourseRegistrations(self):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM COURSE''')
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret
        
    def viewClassRegistrations(self):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM CLASS''')
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret