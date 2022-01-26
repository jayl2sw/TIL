class Person:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name


# p1 = Person           
# p1.name = '원우'          # 이렇게 직접적으로 값을 변경하는 것을 좋아하지 않는다.
# print(p1.name)

p2 = Person('몰라', 20)
p2.set_name('용래')
print(p2.get_name())

p3 = Person('송지', 23)
print(p3._age)              # 이렇게 해도 불러진다. 하지만 암묵적으로 하지 않기로 함

p4 = Person('나야나',22)
print(p4._Person__name)     # 이렇게 하면 불러올 수 있기는 있다. 하지만 그러지 말자