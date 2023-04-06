from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:

    def __init__(self, robot, dinosaur, weapon):
        self.robot = Robot
        self.dinosaur = Dinosaur
        self.weapon = Weapon
        pass

    def run_game(self, robot, dinosaur):
        self.dinosaur = ()
        self.robot = ()
        pass   

    def display_welcome(self):
        print("\nWelcome to the battle of the ages!\nOnly one side can win!\n")


    def battle_phase(self, robot, dinosaur):
        robot.health -= (25)
        dinosaur.health -= (25)      
        pass

    def display_winner(self):
        # print(f"The winner is { }")
            
        pass
    
    

