class Animal: # grandparent
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Prey(Animal): # parent
    def flee(self):
        print(f"{self.name} is fleeing")
        
class Predator(Animal): # parent
    def hunt(self):
        print(f"{self.name} is hunting")
        
class Rabbit(Prey): # children
    pass

class Hawk(Predator): # children
    pass

# children
class Fish(Prey, Predator): # multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.flee()
fish.eat()
fish.sleep()
fish.hunt()