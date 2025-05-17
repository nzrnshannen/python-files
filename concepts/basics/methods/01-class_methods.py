# class methods

class Student:
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    # instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa = {cls.total_gpa/cls.count:.2f}"
    
student1 = Student("Shannen", 3.2)
student2 = Student("Eljoy", 3.1)
student3 = Student("Rosette", 3.3)

print(Student.get_count())
print(Student.get_average_gpa())