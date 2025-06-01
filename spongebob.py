class Student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

student1 = Student("SpongeBob", 20)
student2 = Student("Patrick", 21)

print(student1.name)  # Output: SpongeBob
print(student1.age)   # Output: 20