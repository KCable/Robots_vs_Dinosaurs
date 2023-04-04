from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:

    def __init__(self, robot, dinosaur, weapon):
        self.robot = Robot
        self.dinosaur = Dinosaur
        self.weapon = Weapon
        pass

    def robot(self, dinosaur):
        self.name = ("Marvin")
        self.battle_phase
        dinosaur.health -= (25)


    def dinosaur(self, robot):
        self.name = ("Godzilla")
        self.battle_phase
        robot.health -= (25)

    def weapon(self, weapon):
        weapon.name = ("Ice Ray")
        self.battle_phase    


    def run_game(self, robot, attack):
        self.attackk= attack
        robot.attack = attack
        
 
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


    # def battle_phase(self, robot, dinosaur,):
    #     robot.health -= (25)
    #     dinosaur.health -= (25)
        
    #     pass


    def display_winner(self):
        # print(f"The winner is {}")
              
        pass
    
    

