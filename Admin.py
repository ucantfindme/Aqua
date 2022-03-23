from Person import Person
from Class import Class 
from Student import Student
from Teacher import Teacher
class Admin(Person):
    def __init__(self,name,dob,ph,email,adminId,pas):
        super().__init__(name,dob,ph,email)
        self.adminId=adminId
        self.pas=pas
    def createStudent(self,batch):
        pass
    def createTeacher(self,dept):
        pass
    def createClass(self,studentList,advisor):
        pass
    def createCourse(self,Class,faculty):
        pass
    def viewStudentRegistrations(self):
        pass
    def viewTeacherRegistrations(self):
        pass
    def viewCourseRegistrations(self):
        pass
    def viewClassRegistrations(self):
        pass
    
x=Admin("go","1212",56666,"vasa",101,"ss")

