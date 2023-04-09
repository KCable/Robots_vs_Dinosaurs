from Fleet import Fleet
from Herd import Herd

class Battlefield:

    def __init__(self):
        self.robots = Fleet()
        self.dinosaurs = Herd()
        pass

    def run_game(self):
        self.welcome()
        self.battle_phase()
        self.display_winner()
        pass   

    def welcome(self):
        print("Welcome to the battle!")
        pass

    def battle_phase(self):
        while len(self.dinosaurs.dino_list) > 0 and len(self.robots.robot_list) > 0:
            self.dinosaurs.dino_list[0].attack(self.robots.robot_list[0])
            self.robots.robot_list[0].attack(self.dinosaurs.dino_list[0])
            if self.robots.robot_list[0].hp <= 0:
                print(f"{self.robots.robot_list[0].name} has been defeated!")
                self.robots.robot_list.pop(0)
            if self.dinosaurs.dino_list[0].hp <= 0:
                print(f"{self.dinosaurs.dino_list[0].name} has been defeated!")
                self.dinosaurs.dino_list.pop(0)
            
        pass

    def display_winner(self):
        if len(self.dinosaurs.dino_list) > 0:
            print ("The Dinosaurs are the champions!")
        if len(self.robots.robot_list) > 0:
            print ("The Robots are the champions!")
                    
        pass
    
    

