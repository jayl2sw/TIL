from wiki.pokemon import Pokemon

class Pikachu(Pokemon):
    no = 25
    pika_population = 0

    def __init__(self, name, lv=5):
        super().__init__(name, lv) # 부모 클래스의 init 호출
        self.skill3 = "전기 충격"
        self.increase

    def skill1(self):
        return self.skill1

    def skill3(self):
        return self.skill3

    def pika_increase(cls):
        Pokemon.increase()
        cls.pika_population += 1

pika = Pikachu('피카츄')
# print(pika.skill1)
# print(Pokemon.population)
# print(Pikachu.population)

# print(pika.lv)
# print(pika.no)

# print(pika.skill1)
# print(pika.skill3)


class Metamong(Pokemon):
    no = 132
    meta_population = 0

    def __init__(self, name, lv=5):
        super().__init__(name, lv) # 부모 클래스의 init 호출
        self.skill1 = "변신"

    def skill1(self):
        return self.skill1

    def skill3(self):
        return self.skill3

    def meta_increase(cls):
        Pokemon.increase()
        cls.meta_population += 1


meta = Metamong('피카츄')
print(f"피카츄 인구: {pika.population}")
print(f"메타몽 인구: {meta.population}")

print(f'Pikachu lv:\t{pika.lv}, \tPikachu No: \t{meta.no}, \tSkill1:\t\t{meta.skill1}')
print(f'Metamong lv:\t{meta.lv},\tMetamong No: \t{meta.no},\tSkill1:\t\t{meta.skill1}')


class Child(Pikachu, Metamong):
    pass

c = Child('피카츄?')
print(f"Child No:\t{c.no}, \tChild Skill1:\t{c.skill1}, \tChild Skill3:\t{c.skill3}") # => 피카츄가 앞에 있더라도 메타몽만 오버라이드 했기 때문에 skill1이 변신이 된다.

class Brother(Metamong, Pikachu):
    pass
b = Brother('메타몽?')
print(f"Brother No:\t{b.no}, \tBrother Skill1:\t{b.skill1}, \tBrother Skill3:\t{b.skill3}")