from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health        
        pass

    def attack(self, dinosaur):
        self.active_weapon = dinosaur
        