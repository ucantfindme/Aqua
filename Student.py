from Person import Person
from Course import Course
class Student(Person):
    def __init__(self,name,dob,ph,email,studentid,batch,password):
        super().__init__(name,dob,ph,email)
        self.studentid=studentid
        self.batch=batch
        self.password=password
    def viewCalendar(self):
        pass
    def getAttendance(self,course):
        pass
    def viewRegisteredCourses(self):
        pass
    def viewProfile(self):
        pass
