from weapon import Weapon

class Robot:
    def __init__(self, name, health:int):
        self.name = name
        self.health = health        
        pass

    def attack(self, name, weapon):
        self.name = [0]
        self.active_weapon = weapon

        
        pass

    name = ["R2-D2, Johnny 5, Wall-E, Bumblebee, Marvin"]    
    health = 200
    active_weapon = Weapon
    
        