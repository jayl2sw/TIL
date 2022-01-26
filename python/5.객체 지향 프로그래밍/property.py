class Person:
    def __init__(self,age):
        self._age = age


    @property               # 이걸 통해서 메서드를 정의 했지만
    def age(self):          # 속성처럼 쓰도록 한다.
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return

        self._age = new_age
    
p1 = Person(10)
print(p1.age)