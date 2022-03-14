class Pokemon:
    info = "푸키먼.."
    population = 0

    def __init__(self,name, lv = 1):
        self.name = name
        self.lv = lv
        self.skill1 = "몸통박치기"
        self.skill2 = "꼬리흔들기"
        self.skill3 = None
        self.skill4 = None
        self.info = Pokemon.info + name

        Pokemon.increase()        

    def skill1(self):
        return self.skill1

    @classmethod
    def increase(cls):
        cls.population += 1

