from Weapon import Weapon
from random import choice

class Robot:
    def __init__(self, name):
        self.hp = 100
        self.name = name
        self.weapon_list = [Weapon("Laser Gun", 10), Weapon("Ice Ray", 20), Weapon("Tar Slimer", 30)] 
        self.active_weapon = choice(self.weapon_list)

        pass

    def attack(self, opponent):
        opponent.hp -= self.active_weapon.power
        pass

   
