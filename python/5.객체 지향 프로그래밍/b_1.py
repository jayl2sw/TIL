class Person:
    
    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


jimin = Person()
jimin.name = '지민'
jimin.phone = '01012341234'
jimin.greeting()

hyoeun = Person()
hyoeun.name = '효은'
hyoeun.greeting()
