from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health        

    
    def robot_name(self):
        self.name = ("R2-D2, Bumblebee, Marvin")
        self.display_info()
    
    def active_weapon(self):
        self.active_weapon =  Weapon
        self.display_info()
    
    def health(self):
        self.health = 200
        self.display_info()

robot = Robot
 