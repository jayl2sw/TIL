class Person:
    def __init__(self,age):
        self._age = age


    @property               # 이걸 통해서 메서드를 정의 했지만
    def age(self):          # 속성처럼 쓰도록 한다.
        return self._age    # 주로 getter 정의 할 때는 property로 정의한다.

    @age.getter             # 하위 클래스에서 오버라이드 할 때, 사용한다.
    def age(self):          # Person.age.getter
        return self._age


    @age.setter
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return

        self._age = new_age

class Human(Person):        # Human 클래스만 보아도 Person클래스에 age라는 변수가 있고
    @Person.age.getter      # 해당 변수를 불러오는 함수라는 것을 바로 알 수 있다.
    def age(self):
        return Person._age


p1 = Person(10)
h1 = Human(20)
print(h1.age())
print(p1.age)
