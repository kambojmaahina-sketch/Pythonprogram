'''Student - Properties-rollNo,name,hindi,eng,math,sci,sst,total,
per, constructor, display, 
Note: rollno should be auto generated'''
class Student:
    rollno=101
    count=0 
    def __init__(self,name,hindi,math,eng,sci,sst):
        print("Student constructor called")
        self.Name=name
        self.hindi=hindi
        self.eng=eng
        self.math=math
        self.sci=sci
        self.sst=sst
        self.total= self.hindi+ self.eng+ self.math+ self.sci+ self.sst
        self.per=self.total/5
        Student.rollno+=1
        Student.count+=1
        self.id=Student.count 
    def display(self):
        print("Rollno :", self.rollno)
        print("Name:", self.Name)
        print("Hindi :", self.hindi)
        print("English :", self.eng)
        print("Math :", self.math)
        print("Science :", self.sci)
        print("SST :", self.sst)
        print("Total :", self.total)
        print("Percentage :", self.per)
