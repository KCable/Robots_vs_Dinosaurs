
class Dinosaur:

    def __init__(self, dino_name, attack_power, health):
        self.name = dino_name 
        self.attack =attack_power
        self.health = health
       
    def dino_name(self):
        self.name = ("Rex, Godzilla, Barney")
        self.display_info()
    
    def attack_power(self, attack):
        self.attack -= (25)
        self.display_info()
    
    def health(self):
        self.health = (200)
        self.display_info()

    def attack(self, robot):
        self.attack_power -= (25)
        self.display_info()

dinosaur = Dinosaur



        
        
   

 