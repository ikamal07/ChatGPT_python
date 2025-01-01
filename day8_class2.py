import statistics

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        self.average = 0


    def average_grade(self):
        self.average = statistics.mean(self.grades)

    def is_passing(self):
        self.average_grade()
        if self.average >= 40:
            return True
        else:
            return False

stud1 = Student("Vihan", 30, [8,7,9,55])

print("Student Pass :", stud1.is_passing())
        
        
