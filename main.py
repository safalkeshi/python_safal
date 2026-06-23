
students =[]



class Student:
     
    def __init__(self,name,age,class_no,roll_no,fees,attendance):
         self.name =name
         self.age =age
         self.clas_no =class_no
         self.roll_no =roll_no
         self.attendance =attendance
         self.fees=fees


    def displayinfo(self):
      return (f"roll_no{self.roll_no}:name:{self.name}\n"
              f"attendnce :{self.attendance}")
class StudentManager:
    def __init__(self):()