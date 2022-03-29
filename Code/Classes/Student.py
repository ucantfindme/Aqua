from Person import Person
from Course import Course
class Student(Person):
    def __init__(self,studentid,name,dob,ph,email,batch,type):
        super().__init__(studentid,name,dob,ph,email,type)
        self.batch=batch
    def viewCalendar(self):
        pass
    def getAttendance(self,course):
        pass
    def viewRegisteredCourses(self):
        pass
    def viewProfile(self):
        #open up profile gui for student
        pass
