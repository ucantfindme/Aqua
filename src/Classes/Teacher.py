#import Classes.Person
from Classes import Person,Meeting,Course
import os
import sqlite3
import csv
class Teacher(Person.Person):
    def __init__(self,userid,name,dob,ph,email,type,dept,cou_tau):
        super().__init__(userid,name,dob,ph,email,type)
        self.department=dept
        self.courses_taught=cou_tau
        
    def scheduleMeeting(self,meeting_id,title,conducted_by,course,date,start_time,duration,attendance_report):
        me=Meeting(meeting_id,title,conducted_by,course,date,start_time,duration,attendance_report)
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO MEETING VALUES (?,?,?,?)''',(meeting_id,title,conducted_by,course,date,start_time,duration))
        # Display data inserted
        """print("Data Inserted in the table: ")
        data=cursor.execute('''SELECT * FROM PERSON''')
        for row in data:
            print(row)"""
        #Commit your changes in the database	
        conn.commit()
        #Closing the connection
        conn.close()
        return me
    
    def uploadAttendance(self,meeting,pth=os.path.abspath('.')+"/src/SampleAttendanceReports/s1.csv"):
        eve=[]
        with open(pth) as f:
            reader=csv.reader(f,delimeter=" ")
            for ev in reader:
                eve.append(ev)
        
        
    def viewScheduleMeetings(self):
        pass
    def viewMeetingAttendance(self,meeting):
        pass
    def viewOverallAttendance(self,course):
        pass
    def viewProfile(self):
        pass
    
