from Course import Course
from Student import Student
class Class:
	def __init__(self,ClassId,Advisor,Student,CourseEnrolled):
		self.ClassId=ClassId
		self.Advisor=Advisor
		self.Student=Student
		self.CourseEnrolled=CourseEnrolled
	def addStudent(self,student):
		self.Student.append(student)
		#update this on DB
		return
	def enrollCourse(self,course):
		self.CourseEnrolled.append(course)
		#update this on DB
		 	
