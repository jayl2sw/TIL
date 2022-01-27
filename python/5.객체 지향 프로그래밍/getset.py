class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter                 #getter가 있을때만 setter를 만들 수 있다.
    def age(sef, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return

        self._age = new_age    



p1 = Person(20)
print(p1.age)