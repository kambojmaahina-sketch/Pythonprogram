from rect import Rect
r1=Rect() # Create an instance of Rect
r2=Rect(4,2) #c Create another instance of Rect
r1.length=4
r1.width=5
r1.display() # Dispaly the dimensions of the rectangle 
print(f"Area of Rect{r1.id}:{r1.area()}") #dispalys area
print(f"Perimeter of Rect{r1.id}:{r1.perimeter()}")

r2.display()
print(f"Area of Rect{r2.id}:{r2.area()}") #dispalys area
print(f"Perimeter of Rect{r2.id}:{r2.perimeter()}")

print(f"Total Rect instances created: {Rect.count}") # Displays total num of Rect instances created