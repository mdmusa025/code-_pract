class student:
    def __init__ (self):
       self.roll_no=""
       self.dob=""
       self.gender=""
       self.phone_no=""
       self.email=""
       self.branch=""
       self.course=""
       self.semester=""

class StudentRecord:
    def __init__(self):
        self.list_student_Record=[]
        self.login_username=""
        self.login_password=""

    def add_student_Record(self):
        temp_data=student()
        temp_data.name= input ("enter the student name:")    
        temp_data.roll_no= input ("enter the student roll_no:")
        temp_data.dob= input ("enter the student dob:")    
        temp_data.gender= input ("enter the student gender:")
        temp_data.phone_no= input ("enter the student mobileno:") 
        temp_data.email= input ("enter the student email-id:") 
        temp_data.branch= input ("enter the student branch:")    
        temp_data.course= input ("enter the student course:")
        temp_data.semester= input ("enter the student semester:")     
         
         