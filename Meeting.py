class Meeting:
    def __init__(self,
                 meeting_id,
                 title,
                 conducted_by,
                 course,
                 date,
                 start_time,
                 duration,
                 attendance_report):
        self.meeting_id=meeting_id
        self.title=title
        self.conducted_by=conducted_by
        self.course=course
        self.date=date
        self.start_time=start_time
        self.duration=duration
        self.attendance_report=attendance_report
    def  generateattendance(self):
        pass
    def isPresent(self):
        pass