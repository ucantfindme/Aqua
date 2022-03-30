import Classes.Course
import Classes.Student
class Class:
	def __init__(self,ClassId,Advisor,Students,CourseEnrolled):
		self.ClassId=ClassId
		self.Advisor=Advisor
		self.Students=Students
		self.CourseEnrolled=CourseEnrolled
	def addStudent(self,student):
		self.Students.append(student)
		#update this on DB
		return
	def enrollCourse(self,course):
		self.CourseEnrolled.append(course)
		#update this on DB
		 	
