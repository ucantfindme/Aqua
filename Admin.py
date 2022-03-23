from Person import Person
from Class import Class 
from Student import Student
from Teacher import Teacher
class Admin(Person):
    def __init__(self,name,dob,ph,email,adminId,pas):
        super().__init__(name,dob,ph,email)
        self.adminId=adminId
        self.pas=pas
    def __init__(self,name,dob,ph,email,adminId,pas):
        super().__init__(name,dob,ph,email)
        self.adminId=adminId
        self.pas=pas
        
    def createStudent(self,name,dob,ph,email,studentid,batch,password):
        stu=Student(name,dob,ph,email,studentid,batch,password)
        #update this to DB
        return stu
    
    def createTeacher(self,name,dob,ph,email,teacherId,department,courses_taught,password):
        tea=Teacher(name,dob,ph,email,teacherId,department,courses_taught,password)
        #Add new column to Teacher Table in DB
        return tea
    
    def createClass(self,ClassId,Advisor,Students,CoursesEnrolled):
        cla=Class(ClassId,Advisor,Students,CoursesEnrolled)
        #Add new column to Class Table in DB
        return cla
    
    def viewStudentRegistrations(self):
        pass
    def viewTeacherRegistrations(self):
        pass
    def viewCourseRegistrations(self):
        pass
    def viewClassRegistrations(self):
        pass
    
x=Admin("go","1212",56666,"vasa",101,"ss")

