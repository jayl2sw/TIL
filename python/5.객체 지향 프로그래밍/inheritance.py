"""
class Person:
    population = 0
    
    @staticmethod
    def add_population():
        Person.population += 1

Person.add_population()
print(Person.population)

class Student(Person):
    population = 0

Student.add_population()
print(Student.population)
"""
class Person:
    population = 0
    
    @classmethod
    def add_population(cls):
        cls.population += 1

Person.add_population()
print(Person.population)

class Student(Person):
    population = 0

Student.add_population()
print(Student.population)