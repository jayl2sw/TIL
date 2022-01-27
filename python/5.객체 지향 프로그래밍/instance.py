class Person:

    # 인스턴스 메서드 
    # Python 내부적으로 Person.test(p1)
    # 첫번째 인자로 p1을 넣어준다. self
    def test(self):
        return self

p1 = Person()
s = p1.test()

print(s)