#import Classes.Person
import Classes.Course
import Classes.Meeting
from Classes import Person
class Teacher(Person.Person):
    def __init__(self,userid,name,dob,ph,email,type,dept,cou_tau):
        super().__init__(userid,name,dob,ph,email,type)
        self.department=dept
        self.courses_taught=cou_tau
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
    
