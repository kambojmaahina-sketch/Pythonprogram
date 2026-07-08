'''Box , Properties - l,b,h , consturctor, Box count, display, volume, surface area'''
class Box:
    '''A class representing box with length,breadth and height'''
    count=0 # Class Attribute to keep track of the number of box instances
    def __init__(self,len=1,wid=1,heigh=1):
        '''Initialize new box with default dimenesions'''
        print("Box constructor called")
        self.length=len #Instance attribute
        self.width=wid #Instance attribute
        self.height=heigh #Instance attribute
        Box.count+=1 #increament count of box instance
        self.id=Box.count #assign unique ID to box instance

    def display(self):
        '''Display the dimensions of the box'''
        print(f"Box{self.id} Dimension: {self.length}x{self.width}x{self.height}")
    def area(self):
        '''Calculate and return the area of box'''
        return 2* ((self.length* self.width) + (self.height*self.length) + (self.height*self.width))
    def perimeter(self):
        '''Calculate and return perimeter of box'''
        return 4* (self.length + self.width + self.height)