class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height= height
    
    def __gt__(self, other):
        print(f'{self.name}: {self.age}살 / {other.name}: {other.age}살')
        return self.age > other.age
    
    def __len__(self):
        return self.height

    def __str__(self):
        return f'<{self.name}> : {self.age}살'


p1 = Person('Tom', 100, 180)
p2 = Person('Ben', 10, 178)


print(p1)

print(p1 > p2)
print(len(p1))
print(len(p2))
