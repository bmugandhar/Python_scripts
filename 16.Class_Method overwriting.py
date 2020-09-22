# Methos overwriting 

class Student:        # Parent class 
   def stdinfo(self): 
      print ('Student info Parent class method') 
 
class Subject(Student):  # Child class 
    def subinfo(self):
        print('subject info method in child class')
    def stdinfo(self): 
      print ('student information Child class method') 


c = Subject()          # instance of child class
p = Student()          # instance of Parent class
c.stdinfo()
p.stdinfo()

 
