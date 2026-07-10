class Person:
    count=0 
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender
        print("Person constructor called")
        Person.count+=1
        self.id=Person.count 
    def setname(self,name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    def __str__(self):
        return f"ID={self.id}, Name={self.__name}, Age={self.__age}, Gender={self.__gender}"