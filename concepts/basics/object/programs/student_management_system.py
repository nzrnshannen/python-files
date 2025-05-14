# student management system

class Student: 
    def __init__(self, name, studentID, grades):
        self.name = name
        self.studentID = studentID
        self.grades = grades
        
    def displayStudDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.studentID}")
        print("Grades:", end = " ")
            
        for grade in self.grades:
            print(grade, end=" ")
            
    def averageGrade(self):
        ave = total = 0
        for grade in self.grades:
            total += grade
                
        ave = total / len(self.grades)
            
        print(f"\nAverage: {ave}")
            
student1 = Student("Shannen", "19103991", [90, 91, 98, 95, 89])
student2 = Student("Prince", "Bendoy", [89, 90, 97, 94, 89])

student1.displayStudDetails()
student1.averageGrade()

student2.displayStudDetails()
student2.averageGrade()