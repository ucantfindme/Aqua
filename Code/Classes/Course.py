import Classes.Student
import Classes.Meeting
class Course:
	def __init__(self,CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll):
		self.CourseId=CourseId
		self.Title=Title
		self.Prerequisites=Prerequisites
		self.ClassEnrolled=ClassEnrolled
		self.FacultyAssigned=FacultyAssigned
		self.LectureAll=LectureAll
	def getMeetingAttendance(self,Meeting):
		pass
	def getStudentAttendance(self,student):
		pass			 
