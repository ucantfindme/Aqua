import sqlite3
import Classes.Student
import Classes.Meeting
import os
import sqlite3
from Classes import Meeting
class Course:
	def __init__(self,CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll):
		self.CourseId=CourseId
		self.Title=Title
		self.Prerequisites=Prerequisites
		self.ClassEnrolled=ClassEnrolled
		self.FacultyAssigned=FacultyAssigned
		self.LectureAll=LectureAll
  
	def getMeetingAttendance(self,meeting):
		path=os.path.abspath('.')+"/src/DB"
		conn = sqlite3.connect(path+'/person.db')
		cursor = conn.cursor()
		#print(meeting)
		lst=cursor.execute('''SELECT ATT_REPORT FROM MEETING WHERE MEETINGID=?''',(meeting))
		ret=[list(i) for i in lst]
		conn.commit()
		conn.close()
		return ret[0]

	def getStudentAttendance(self,student):
		att=0
		tot=0
		for i in self.LectureAll:
			tot+=1
			path=os.path.abspath('.')+"/src/DB"
			conn = sqlite3.connect(path+'/person.db')
			cursor = conn.cursor()
			lst=cursor.execute('''SELECT * FROM MEETING WHERE MEETINGID=?''',(i))
			for j in lst:
				meeting_id,title,conducted_by,course,date,start_time,duration,attendance_report=j
			met=Meeting.Meeting(meeting_id,title,conducted_by,course,date,start_time,duration,attendance_report)
			if met.isPresent(student):
				att+=1
			conn.commit()
			conn.close()
		return (att,tot)
