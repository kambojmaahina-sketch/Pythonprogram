class Rect:
    '''A class representing rectangle with width and height'''
    count=0 # Class Attribute to keep track of the number of Rect instances
    def __init__(self,len=1,wid=1):
        '''Initialize new rectangle with default dimenesions'''
        print("Rect constructor called")
        self.length=len #Instance attribute
        self.width=wid #Instance attribute
        Rect.count+=1 #increament count of rectangle instance
        self.id=Rect.count #assign unique ID to rect instance

    def display(self):
        '''Display the dimensions of the rectangle'''
        print(f"Rect{self.id} Dimension: {self.length}x{self.width}")
    def area(self):
        '''Calculate and return the area of rectangle'''
        return self.length* self.width
    def perimeter(self):
        '''Calculate and return perimeter of rectangle'''
        return 2* (self.length + self.width)