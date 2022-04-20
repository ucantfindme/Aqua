import Classes.Course
import Classes.Student
import os
import sqlite3
class Class:
	def __init__(self,ClassId,Advisor,Students,CourseEnrolled):
		self.ClassId=ClassId
		self.Advisor=Advisor
		self.Students=Students
		self.CourseEnrolled=CourseEnrolled
	def addStudent(self,student):
		self.Students.append(student)
		path=os.path.abspath('.')+"/src/DB"
		conn = sqlite3.connect(path+'/person.db')
		cursor = conn.cursor()
		cursor.execute('''UPDATE CLASS SET STUDENTS=? WHERE CLASSID=?''',(self.Students,self.ClassId))
        #Commit your changes in the database	
		conn.commit()
        #Closing the connection
		conn.close()
		return
	def enrollCourse(self,course):
		self.CourseEnrolled.append(course)
		#update this on DB
		path=os.path.abspath('.')+"/src/DB"
		conn = sqlite3.connect(path+'/person.db')
		cursor = conn.cursor()
		cursor.execute('''UPDATE CLASS SET COURSES_ENROLLED=? WHERE CLASSID=?''',(self.CourseEnrolled,self.ClassId))
        #Commit your changes in the database	
		conn.commit()
        #Closing the connection
		conn.close()
		return
