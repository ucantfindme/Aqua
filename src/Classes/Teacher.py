#import Classes.Person

from Classes import Person,Meeting,Course,Attendance,Class
import os
import sqlite3
import csv

class Teacher(Person.Person):
    def __init__(self,userid="KKumar",name="KrishnaKumar",dob="7-6-1990",ph="33256",email="krishna3@gmail.com",type='T',dept="CSE",cou_tau="OS,SE"):
        super().__init__(userid,name,dob,ph,email,type)
        self.department=dept
        self.courses_taught=cou_tau
        
    def scheduleMeeting(self,meeting_id,title,conducted_by,course,date,start_time,duration):
        me=Meeting.Meeting(meeting_id,title,conducted_by,course,date,start_time,duration)
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO MEETING VALUES (?,?,?,?,?,?,?,"set()")''',(meeting_id,title,conducted_by,course,date,start_time,duration))
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
    
    def uploadAttendance(meetingid,pth=os.path.abspath('.')+"/src/SampleAttendanceReports/s1.csv"):
        #print(pth)
        eve=[]
        with open(pth,"r",encoding="utf8", errors='ignore') as f:
            reader=csv.reader(x.replace('\0',"") for x in f)
            for ev in reader:
                if ev:
                    #print(ev[0].split('\t')[0])
                    eve.append(ev[0].split('\t')[0])
        pres=set()
        for i in eve[1:]:
            pres.add(i)
        #print(len(pres))
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE MEETING SET ATT_REPORT=? WHERE MEETINGID=?''',[str(pres),meetingid])
        conn.commit()
        for i in pres:
            #print(i)
            t=len(list(cursor.execute('''SELECT * FROM ATTENDANCE''')))
            #at=Attendance.Attendance(t+1,i,meetingid,1,True)
            cursor.execute('''INSERT INTO ATTENDANCE VALUES (?,?,?)''',(t+1,i,meetingid))
        conn.commit()
        #Closing the connection
        conn.close()
        return pres
            
    def viewScheduleMeetings(self):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM MEETING WHERE COND_BY=? and ATT_REPORT="set()" ''',[self.userid])
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret
    
    def viewMeetingAttendance(self,meeting):
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        print(meeting)
        lst=cursor.execute('''SELECT ATT_REPORT FROM MEETING WHERE MEETINGID=?''',[meeting])
        ret=[list(i) for i in lst]
        conn.commit()
        conn.close()
        return ret[0]
    
    def viewOverallAttendance(self,course):
        ret=[]
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll='0','0','0','0','0','0'
        lst=cursor.execute('''SELECT * FROM COURSE WHERE COURSEID=?''',[course])
        for i in lst:
            CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll=i
        lst=cursor.execute('''SELECT * FROM CLASS WHERE CLASSID=?''',[ClassEnrolled])
        for i in lst:
            ClassId,Advisor,Students,CourseEnrolled=i
        conn.close()
        co=Course.Course(CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll)
        d=dict()
        for i in Students:
            d[i]=co.getStudentAttendance(i)
        return d.items()
    
    def viewProfile(self):
        return [self.id,self.usertype,self.name,self.dob,self.ph,self.email,self.department,self.courses_taught]
    
