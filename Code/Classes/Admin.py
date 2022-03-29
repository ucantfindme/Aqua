
from Classes import Person, Student, Teacher, Class, Course
class Admin(Person.Person):
    def __init__(self,userid,name,dob,ph,email,type):
        super().__init__(userid,name,dob,ph,email,type)
        
    def createStudent(self,studentid,name,dob,ph,email,batch,password):
        stu=Student.Student(studentid,name,dob,ph,email,batch,password)
        #update this to DB
        return stu
    
    def createTeacher(self,name,dob,ph,email,teacherId,department,courses_taught,password):
        tea=Teacher.Teacher(name,dob,ph,email,teacherId,department,courses_taught,password)
        #Add new column to Teacher Table in DB
        return tea
    
    def createClass(self,ClassId,Advisor,Students,CoursesEnrolled):
        cla=Class.Class(ClassId,Advisor,Students,CoursesEnrolled)
        #Add new column to Class Table in DB
        return cla
    
    def createCourse(self,classid,Title,Prerequisites,ClassEnrolled,FacultyAssigned):
        cou=Course.Course(classid,Title,Prerequisites,ClassEnrolled,FacultyAssigned,[])
        #Add new column to Course Table in DB
        return cou
    
    def viewStudentRegistrations(self):
        pass
    def viewTeacherRegistrations(self):
        pass
    def viewCourseRegistrations(self):
        pass
    def viewClassRegistrations(self):
        pass
    
x=Admin("go","1212",56666,"vasa",101,"ss")

