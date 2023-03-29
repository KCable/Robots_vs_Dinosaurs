from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur
        self.weapon = Weapon
        pass

    def run_game(self, dinosaur, robot):

       #Full Layout of Battle


        pass
        

    def display_welcome(self):
        print("\nWelcome to the battle of the ages!\nOnly one side can win!\n")


    def battle_phase(self, attack_power:int):
        self.attack -= attack_power
        
        pass


    def display_winner(self):
        pass