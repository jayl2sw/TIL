from wiki.pokemon import Pokemon

class Metamong(Pokemon):
    no = 132
    def __init__(self, name, lv=5):
        super().__init__(name, lv) # 부모 클래스의 init 호출
        self.skill1 = "변신"

    def skill1(self):
        return self.skill1

    def skill3(self):
        return self.skill3


pika = Pikachu('피카츄')
print(pika.skill1)
print(Pokemon.population)
print(Metamong.population)

print(pika.lv)
print(pika.no)

print(pika.skill1)
print(pika.skill3)

