class character():
    def __init__(self,name,RPGClass):
        self.name = name
        self.RPGClass = RPGClass
        self.life = 5
        self.agility = 2
        self.strength = 2
        self.wit = 2

    def attack(self):
        self.sentence = "Rrrrrrrrr...."
        print (self.name, ':', self.sentence)

users = character ("Jean-Luc","Character")
users.attack()
