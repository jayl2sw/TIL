class Person:
    # 클래스 속성
    # 모든 인스턴스의 공통 속성
    __population = 0    # __를 붙이면 비공개 변수로 만든다 
                        # 비공개 변수는 Class 내에서만 불러올 수 있다.
    
    # 생성자 
    # 특별한 데코레이터가 없는 메서드는
    # 인스턴스 메서드고,
    # 인스턴스의 속성 또는 값을 조작하는 행위를 위한 메서드
    # 첫번째 인자로는 인스턴스 자신이 오게 될 것이다.
    # self라는 이름은 관례적인 것이고, 바뀌어도 문제는 없다.
    # 하지만 바꾸지는 않을 것이다.
    def __init__(self, name):
        # 인스턴스 속성
        self.name = name
        # self.population => 인스턴스의 속성이 되어버린다.
        # Person.population += 1    # 되긴 된다. 하지만 이건 밖에서 Person.population += 1하는 것과 같다.
                                    # 그래서 인스턴스 메서드에서는 클래스 속성을 건드리지 않는다.
        # Person.increase()
        self.increase()

    def __del__(self):
        print('으악')
        self.decrease()


    @classmethod
    def increase(cls):              # 클래스 또는 인스턴스 활용해서 호출
        cls.__population += 1       # 해당 클래스에 속해있는 속성만 바꿀 수 있다.
        print(cls.__population)
    
    @classmethod
    def decrease(cls):          
        cls.__population -= 1
        print(cls.__population)
    
    @staticmethod                   # 스태틱 매서드는 클래스의 공통 속성은 웬만하면 건드리지 말아야 한다.
    def decrease():                 # 속성 변경 외에 다른 어떠한 일들을 할 때, 스태틱 메서드를 사용한다.
        # Person.population -= 1
        return '인구 감수가 일어나고 있다.'




class Human(Person):
    pass

# a = Human('휴먼')
kim = Person('김구현')
# kim 인스턴스는 name 속성을 처음 생성할 때 할당되어서 가지게 된다.
print(kim.name)
hong = Person('홍길동')
print(hong.name)
# print(Person.population)

# 클래스 매서드지만 인스턴스 호출 가능
# kim 은 Person의 인스턴스이기 때문
# 하지만 보통 인스턴스로 호출 하지 않는다.
# kim.increase()
# print(Person.population)

# Person.increase()
# print(Person.population)

# print(a.name)
# print(a.population)
# a.increase()        # Human의 population은 증가하지만 Person의 population은 증가하지 않는다.

# print(a.population)
# print(kim.population)

# a.decrease()
# print(a.population)
# print(Person.popultaion)

p1 = Person('Tom')
# Person.__population += 1      # 비공개 변수에 대해서 Class 밖에서는 호출 불가능

# __name__ => 이름은 파일 이름
# if __name__ == '__main__':
# 시험을 동작시키는 파일이 main이면~ 실행

