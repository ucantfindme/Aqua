import Classes.Person
import Classes.Course
from Classes import Person,Course
class Student(Person.Person):
    def __init__(self,userid,name,dob,ph,email,type,batch):
        super().__init__(userid,name,dob,ph,email,type)
        self.batch=batch
        
    def viewCalendar(self):
        pass
    
    def getAttendance(self,course):
        ret=[]
        path=os.path.abspath('.')+"/src/DB"
        conn = sqlite3.connect(path+'/person.db')
        cursor = conn.cursor()
        lst=cursor.execute('''SELECT * FROM COURSE WHERE COURSEID=?''',(course))
        for i in lst:
            CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll=i
        lst=cursor.execute('''SELECT * FROM CLASS WHERE CLASSID=?''',(ClassEnrolled))
        for i in lst:
            ClassId,Advisor,Students,CourseEnrolled=i
        conn.close()
        co=Course.Course(CourseId,Title,Prerequisites,ClassEnrolled,FacultyAssigned,LectureAll)
        return co.getStudentAttendance(self.id)
    
    def viewRegisteredCourses(self):
        pass
    
    def viewProfile(self):
        return [self.id,self.usertype,self.name,self.dob,self.ph,self.email,self.batch]
    
