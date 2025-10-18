class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")



class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)  # Inherit from Student
        self.degree = degree



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade  

    def get_grade(self):
        return self.__grade  

    def set_grade(self, new_grade):
        self.__grade = new_grade  

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.__grade}")



class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    # overriding the display_info method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.get_grade()}, Degree: {self.degree}")



# Creating objects
student1 = Student("Serwaah Johnson", 20, "A")
student2 = Student("James Duntu", 21, "B+")
grad_student = GraduateStudent("Micheal Kofi", 23, "A", "BSc Computer Science")

# Displaying details
student1.display_info()
student2.display_info()
grad_student.display_info()

# Changing grade using setter
student1.set_grade("A+")
print("\nAfter updating Serwaah's grade:")
student1.display_info()
