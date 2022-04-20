class Attendance:
    def __init__(self,attendance_id,studentid,meetingid,timeSpent,present):
        self.attendance_id=attendance_id
        self.meetingid=meetingid
        self.studentid=studentid
        self.timeSpent=timeSpent
        self.present=present
    def giveAttendance(self):
        self.present=True
