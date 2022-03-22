class  Course:
	def __init__(self,CourseId,Title,Pre-requisites,ClassEnrolled,FacultyAssigned,LecturesAll):
		self.CourseId=CourseId
		self.Title=Title
		self.Pre-requisites=Pre-requisites
		self.ClassEnrolled=ClassEnrolled
		self.FacultyAssigned=FacultyAssigned
		self.LectureAll=LectureAll
	def getMeetingAttendance(self,Meeting):
		pass
	def getStudentAttendance(self,student):
		pass			 
