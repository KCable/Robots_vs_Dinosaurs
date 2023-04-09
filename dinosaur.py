from random import choice
from Attack import Attack

class Dinosaur:

    def __init__(self,name):
        self.hp = 100
        self.name = name
        self.attack_list = [Attack("Spike", 10), Attack("Bite", 20), Attack("Stomp", 30)]
        self.active_attack = choice(self.attack_list)
        pass
        





        
        
   

 