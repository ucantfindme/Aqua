# Import module
import sqlite3
import os
# Connecting to sqlite
path=os.path.abspath('.')+"/src/DB"
#print(path)
#exit()

#create logs table to store login details in login.db

conn = sqlite3.connect(path+'/login.db')
cursor = conn.cursor()
table ="""CREATE TABLE LOGS(USERNAME VARCHAR(15),PASS VARCHAR(15),USERTYPE CHAR);"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO LOGS VALUES ('Admin347', 'ad@452', 'A')''')
cursor.execute('''INSERT INTO LOGS VALUES ('NaSaPaKri', 'mikupappa', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('NSPKrishna', 'Maipappa', 'T')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Admin101', 'user@637', 'A')''')
cursor.execute('''INSERT INTO LOGS VALUES ('JKumar', 'jkumar@5659', 'T')''')
cursor.execute('''INSERT INTO LOGS VALUES ('PLela', 'lela12', 'T')''')
cursor.execute('''INSERT INTO LOGS VALUES ('SKrishna', 'sarankrishna', 'T')''')
cursor.execute('''INSERT INTO LOGS VALUES ('KKumar', 'Kumar1234', 'T')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Nobrain', 'Pranee789', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('AJKrishna', 'ajkrish579', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('RajeevRJ', 'rjrajeev18', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('PKrishna', 'pa1sai', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Sanketh12', '165@sanketh', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Harthik07', 'marin', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Varun36', 'emiliya598', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES (Bhargav11', 'ram!198', 'S')''')
cursor.execute('''INSERT INTO LOGS VALUES ('Deepti', 'deepti@317', 'S')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM LOGS''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create person table to store person details in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE PERSON(USERID VARCHAR(15),NAME VARCHAR(255), DOB VARCHAR(255),PHONE NUMBER,EMAIL VARCHAR(255),USERTYPE CHAR);"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO PERSON VALUES ('Admin102', 'Pavan','12-06-2000',12345,'abc@gmail.com', 'A')''')
cursor.execute('''INSERT INTO PERSON VALUES ('NaSaPaKri', 'Sai','12-06-1900',12345,'def@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('NSPKrishna', 'Krishna','12-06-2010',12345,'ghi@gmail.com', 'T')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Admin101', 'Abhi','01-01-2000',56653,'abhi@gmail.com','A')''')
cursor.execute('''INSERT INTO PERSON VALUES ('JKumar', 'Jayakumar','02-06-1980',96542,'jaya@gamil.com', 'T')''')
cursor.execute('''INSERT INTO PERSON VALUES ('PLela', 'Prabha Lela','26-5-1980',46963,'lela@gmail.com', 'T')''')
cursor.execute('''INSERT INTO PERSON VALUES ('SKrishna', 'Saran','18-03-2000',23365,'saran@gmail.com', 'T')''')
cursor.execute('''INSERT INTO PERSON VALUES ('KKumar', 'KrishnaKumar','7-6-1990',33256,'krishna3@gmail.com', 'T')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Nobrain', 'Praneeth','17-5-2002',98875,'nobrain@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('AJKrishna', 'Ajaykrishna','27-9-2001',65462,'ajay@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('RajeevRJ', 'Rajeev','22-6-2001',80233,'rajeev@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('PKrishna', 'PavanKrishna','12-6-2000',55654,'pavan@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Sanketh12', 'Sanketh','21-11-1999',551636,'sanki@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Harthik07', 'Harthik','7-7-2007',972737,'harthik@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Varun36', 'Varun','3-6-2001',56666,'varun@gamil.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Bhargav11', 'Bhargav','9-3-2002',56511,'bhargav@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('Deepti', 'Deepti Hada','9-6-2002',63015,'deepti@gmail.com', 'S')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Admin table in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE ADMIN(USERID VARCHAR(15),NAME VARCHAR(15),ADMINID VARCHAR(15));"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin102', 'Pavan', 'AD1')''')
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin101', 'Abhi', 'AD2')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Student table in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE STUDENT(USERID VARCHAR(15),NAME VARCHAR(15),BATCH VARCHAR(15));"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('NaSaPaKri', 'Sai', 'CSED')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Nobrain', 'Praneeth', 'CSEB')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('AJKrishna', 'Ajaykrishna', 'CSEA')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('RajeevRJ', 'Rajeev', 'ECEA')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('PKrishna', 'PavanKrishna', 'CSEA')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sanketh12', 'Sanketh', 'CSEC')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Harthik07', 'Harthik', 'CSEC')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Varun36', 'Varun', 'CSED')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Bhargav11', 'Bhargav', 'ECEA')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Deepti', 'Deepti Hada', 'CSEB')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Teacher table in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE TEACHER(USERID VARCHAR(15),NAME VARCHAR(15),DEPT VARCHAR(15),COURSES_TAUGHT VARCHAR(255));"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO TEACHER VALUES ('NSPKrishna', 'Krishna', 'CSE', 'PPL,CS')''')
cursor.execute('''INSERT INTO TEACHER VALUES ('Jkumar', 'JayaKumar', 'CSE', 'DSA,DAA')''')
cursor.execute('''INSERT INTO TEACHER VALUES ('PLela', 'Prabha Lela', 'ECE', 'SAS,DE,AEC')''')
cursor.execute('''INSERT INTO TEACHER VALUES (SKrishna', 'Saran', 'CSE', 'CS,DBMS')''')
cursor.execute('''INSERT INTO TEACHER VALUES ('KKumar', 'KrishnaKumar', 'CSE', 'OS,SE')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Class table in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE CLASS(CLASSID VARCHAR(15),ADVISOR VARCHAR(15),STUDENTS VARCHAR(1023),COURSES_ENROLLED VARCHAR(255));"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO CLASS VALUES ('CSED', 'NSPKrishna', 'NaSaPaKri,Varun36', 'CS,DS,PPL')''')
cursor.execute('''INSERT INTO CLASS VALUES ('CSEB', 'KKumar', 'Nobrain,Deepti', 'OS,SE,DAA')''')
cursor.execute('''INSERT INTO CLASS VALUES ('CSEA', 'SKrishna', 'AJKrishna,PKrishna', 'DS,PPL,DSA')''')
cursor.execute('''INSERT INTO CLASS VALUES ('ECEB', 'PLela', 'Bhargav11,RajeevRj', 'SAS,DE,AEC')''')
cursor.execute('''INSERT INTO CLASS VALUES ('CSEC', 'JKumar', 'Harthik07,Sanketh12', 'DAA,DBMS,DSA')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Course table in person.db

conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
table ="""CREATE TABLE COURSE(COURSEID VARCHAR(15),TITLE VARCHAR(63),Prerequisites VARCHAR(255),CLASS_ENROLLED VARCHAR(15),FACULTY_ASSIGNED VARCHAR(15),LECTURES VARCHAR(1023));"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO COURSE VALUES ('PPL','Principles of Programming Languages','','CSED,CSEA','NSPKrishna','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('CS','Computer Security','','CSED,CSEA','NSPKrishna','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('DS',Distributed Systems','','CSED,CSEA','NSPKrishna','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('OS','Operating Systems','','CSEB','KKumar','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('SE','Software Engineering','','CSEB','KKumar','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('DAA','Design Analytics and Algorithms','','CSEB,CSEC','JKumar','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('DSA','Data Structures and Algorithms','','CSEA,CSEC','JKumar','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('DBMS','Data Base Management System','','CSEC','SKrishna','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('SAS','Signals and Systems','','ECEA','PLela','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('DE','Digital Electronics','','ECEA','PLela','')''')
cursor.execute('''INSERT INTO COURSE VALUES ('ACE','Analog Electronic Circuits','','ECEA','PLela','')''')
# Display data inserted
"""print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM PERSON''')
for row in data:
	print(row)"""
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Meeting table in person.db
conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE MEETING (MEETINGID VARCHAR(15),TITLE VARCHAR(32),COND_BY VARCHAR(15),COURSE VARCHAR(15),DATE VARCHAR(15),START_TIME VARCHAR(15),DURATION INTEGER,ATT_REPORT VARCHAR(15))''')
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()

#create Attendance table in person.db
conn = sqlite3.connect(path+'/person.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE ATTENDANCE (ATTENDANCEID INTEGER,STUDENTID VARCHAR(15),MEETINGID VARCHAR(15))''')
#Commit your changes in the database	
conn.commit()
#Closing the connection
conn.close()