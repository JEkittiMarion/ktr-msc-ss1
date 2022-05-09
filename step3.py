class Character():
    def __init__(self,name,RPGClass):
        self.name = name
        self.RPGClass = RPGClass
        self.life = 5
        self.agility = 2
        self.strength = 2
        self.wit = 2

    def attack(self):
        self.sentence = "Rrrrrr....."
        print (self.name, ':', self.sentence)

    #class Movable(self):
    def moveRight(self):
        print (self.name,': moves right')
    def moveLeft(self):
        print (self.name,': moves left')
    def moveBack(self):
        print (self.name,': moves back')
    def moveForward(self):
        print (self.name,': moves forward')

class Warrior (Character):
    def __init__(self,name):
        self.name = name
        self.RPGClass = "Warrior"
        self.life = 100
        self.agility = 8
        self.strength = 10
        self.wit = 3

    def attack(self,weapon):
        if weapon == "hammer":
            print (self.name, ': I ll crush you with my', weapon,'!')
        elif weapon == "sword":
            print (self.name, ': I ll crush you with my', weapon,'!')
        else:
            print (self.name," cant attack")
        

class Mage (Character):
    def __init__(self,name):
        self.name = name
        self.RPGClass = "Mage"
        self.life = 70
        self.agility = 10
        self.strength = 3
        self.wit = 10

    def attack(self,weapon):
        if weapon == "magic":
            print (self.name, ': Feel the power of my', weapon,'!')
        elif weapon == "wand":
            print (self.name, ': Feel the power of my', weapon,'!')
        else:
            print (self.name," cant attack")


users = Character ("Jean-Luc","Character")
users.attack()
warrior = Warrior("Jean")
warrior.attack("sword")
warrior.moveRight()
mage = Mage("Luc")
mage.attack("wan")
mage.moveForward()
