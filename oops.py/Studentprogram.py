from student import Student
s1 = Student("Sushma", 90, 85, 95, 88, 92)
s2 = Student("Rahul", 75, 80, 70, 78, 82)
s1.display()
print()
s2.display()

print(f"Total Studnet instances created: {Student.count}")