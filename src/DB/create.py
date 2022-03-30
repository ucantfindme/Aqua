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
cursor.execute('''INSERT INTO LOGS VALUES ('Admin347', 'Ad@452', 'A')''')
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
cursor.execute('''INSERT INTO PERSON VALUES ('Admin347', 'Pavan','12-06-2000',12345,'abc@gmail.com', 'A')''')
cursor.execute('''INSERT INTO PERSON VALUES ('NaSaPaKri', 'Sai','12-06-1900',12345,'def@gmail.com', 'S')''')
cursor.execute('''INSERT INTO PERSON VALUES ('NSPKrishna', 'Krishna','12-06-2010',12345,'ghi@gmail.com', 'T')''')
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
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin347', 'Pavan', 'AD1')''')
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin336', 'Varun', 'AD2')''')
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin313', 'Bhargav', 'AD3')''')
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin317', 'Deepti', 'AD4')''')
cursor.execute('''INSERT INTO ADMIN VALUES ('Admin359', 'Gopi', 'AD5')''')
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
cursor.execute('''INSERT INTO TEACHER VALUES ('NSPKrishna', 'Krishna', 'CSE', 'OS,SNA,DSA,DAA')''')
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
cursor.execute('''INSERT INTO CLASS VALUES ('CSED', 'NSPKrishna', 'NaSaPaKri,Nobrain,AJKrishna,PKrishna,Varun36,Deepti,Bhargav11,Harthik07,Sanketh12', 'CS,DS,SE,SNA,DL,PPL')''')
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
cursor.execute('''INSERT INTO COURSE VALUES ('PPL','Principles of Programming Languages','PSAT,OOPS,DSA','CSED','NSPKrishna','')''')
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

#create Attendance table in person.db
