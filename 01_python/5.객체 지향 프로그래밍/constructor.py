class Person:
    def __init__(self, name, age=1):
        # 인스턴스 변수를 정의하기 위해 사용!
        # 인스턴스 변수 만들 때 자동으로 호춣 됨
        self.name = name
        self.age = age
        print("응애!")
    
    def __del__(self):
        print("으억...")

p1 = Person('Tom', 222)

# TypeError __init__() missing 2 required positioinal argument: 'name' and 'age'

young = Person('영택', 100)



