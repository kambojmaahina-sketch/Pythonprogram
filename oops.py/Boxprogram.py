from box import Box
b1=Box()
b2=Box(4,2)
b1.length=4
b1.width=5
b1.height=3
b1.display() 
print(f"Area of Rect{b1.id}:{b1.area()}")
print(f"Perimeter of Rect{b1.id}:{b1.perimeter()}")

b2.display()
print(f"Area of Rect{b2.id}:{b2.area()}")
print(f"Perimeter of Rect{b2.id}:{b2.perimeter()}")

print(f"Total Box instances created: {Box.count}")