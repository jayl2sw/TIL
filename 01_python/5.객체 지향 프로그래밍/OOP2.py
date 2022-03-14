class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


p1 = Person('윤경', 30)
p1.talk()

"""
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.deparment = department
    

prof = Professor('김교수', 50, '컴공')
prof.talk()
"""

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.deparment = department

prof = Professor('김교수', 50, '컴공')
prof.talk()

class Student(Person):

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):
        print(f'충성충성! {self.name}입니다. 교수님 ^^')
s1 = Student('승운', 20, 4.5)
s1.talk()

print(isinstance(Professor, Person))
print(isinstance(prof, Person))
print(issubclass(Professor, Person))
print(issubclass(bool, int))
print(issubclass(float, int))

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

t1 = Teacher('김보경', 25, 541236)
print(t1.name)