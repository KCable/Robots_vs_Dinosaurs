from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:

    def __init__(self, robot, dinosaur, weapon):
        self.robot = Robot
        self.dinosaur = Dinosaur
        self.weapon = Weapon
        pass

    def robot(self):
        self.name = ("Marvin")
        self.battle_phase


    def dinosaur(self):
        self.name = ("Godzilla")
        self.battle_phase

    def weapon(self):
        self.name = ("Ice Ray")
        self.battle_phase    


    def run_game(self, dinosaur, robot):
        dinosaur.attack = (25)
        robot.attack = (25)
 
    def dino_name(self):
        self.name = ("Rex, Godzilla, Barney")
        self.display_info()
    
    def attack_power(self):
        self.attack_power = 25
        self.display_info()
    
    def health(self):
        self.health = 200
        self.display_info()
       

    def display_welcome(self):
        print("\nWelcome to the battle of the ages!\nOnly one side can win!\n")


    def battle_phase(self, attack_power:int):
        self.attack -= attack_power
        
        pass


    def display_winner(self):
        # print(f"The winner is {}")
              
        pass
    
    

