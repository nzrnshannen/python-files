class Student:
    
    class_year = 2028
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Shannen", 22)
student2 = Student("Eljoy", 19)
student3 = Student("Rosette", 1)
student4 = Student("Lincoln", 2)

print(student1.name, student1.age)
print(student1.class_year)
print(student2.class_year)
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")