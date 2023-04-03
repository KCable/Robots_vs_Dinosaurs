
class Dinosaur:

    def __init__(self, dino_name, attack_power:int, health:int):
        self.name = dino_name 
        self.attack_power = attack_power
        self.health = health
       
    def dino_name(self):
        self.name = ("Rex, Godzilla, Barney")
        self.display_info()
    
    def attack_power(self):
        self.attack_power = 25
        self.display_info()
    
    def health(self):
        self.health = 200
        self.display_info()
  

dinosaur = Dinosaur


    # def attack(self):
        
        
   

 