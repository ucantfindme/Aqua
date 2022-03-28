from Person import Person
from Course import Course
from Meeting import Meeting
class Teacher(Person):
    def __init__(self,name,dob,ph,email,teacherId,department,courses_taught,password):
        super().__init__(name,dob,ph,email)
        self.teacherId=teacherId
        self.department=department
        self.courses_taught=courses_taught
        self.password=password
    def scheduleMeeting(self,course,date):
        pass
    def uploadAttendance(self,meeting):
        pass
    def viewScheduleMeetings(self):
        pass
    def viewMeetingAttendance(self,meeting):
        pass
    def viewOverallAttendance(self,course):
        pass
    def viewProfile(self):
        pass
    
