import Classes.Person
import Classes.Course
from Classes import Person
class Student(Person.Person):
    def __init__(self,userid,name,dob,ph,email,type,batch):
        super().__init__(userid,name,dob,ph,email,type)
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
