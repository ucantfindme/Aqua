import sqlite3
class Person:
    def __init__(self,userid,name,dob,ph,email,type):
        self.id=userid
        self.name=name
        self.dob=dob
        self.ph=ph
        self.email=email
        self.usertype=type
    def updateDetails(self,name,dob,ph,email):
        conn = sqlite3.connect('/Users/nspk/Desktop/Aqua/Code/DB/person.db')
        cursor = conn.cursor()
        val=cursor.execute('''UPDATE PERSON SET NAME=?,DOB=?,PHONE=?,EMAIL=? WHERE USERID=? AND USERTYPE=?''',(name,dob,ph,email,self.id,self.usertype))
        #pop-up for successfull updation
        print("Details Updated")
        conn.commit()
        conn.close()
    def updatePassword(self,newpass):
        conn = sqlite3.connect('/Users/nspk/Desktop/Aqua/Code/DB/login.db')
        cursor = conn.cursor()
        val=cursor.execute('''UPDATE LOGS SET PASS=? WHERE USERNAME=? AND USERTYPE=?''',(newpass,self.id,self.usertype))
        #pop-up for successfull updation
        print("Password Updated")
        conn.commit()
        conn.close()

p=Person("NaSaPaKri","Sai","12-06-1900",12345,"def@gmail.com",'S')
p.updateDetails("Sai","12-06-1990",12345,"def@gmail.com")
p.updatePassword("mikupappa")