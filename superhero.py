# Superhero class to handle the strength & health
class Superhero:
    def __init__(self, name, superpower, strength, health):
        self.name = name
        self.superpower = superpower
        self.strength = strength
        self.health = health
        
    # Lose 10 points on strength after fighting
    def attack(self, villain):
        print(f"{self.name} attacks {villain} with {self.superpower}!")
        self.strength -= 10
        
    # Heal 20 points on health after fighting
    def heal(self):
        print(f"{self.name} is healing.")
        self.health += 20
        
    def display_info(self):
        print(f"Hero: {self.name}\nPower: {self.superpower}\nStrength: {self.strength}\nHealth: {self.health}\n")
        
# Speadster inheriting from Superhero
class Speedster(Superhero):
    def __init__(self, name, strength, health):
        super().__init__(name, "Super Speed", strength, health)
    
    def attack(self, villain):
        print(f"{self.name} blitzes around {villain} at lightning speed!")
        self.strength -= 5

# Flyer inheriting from Superhero
class Flyer(Superhero):
    def __init__(self, name, strength, health):
        super().__init__(name, "Flight", strength, health)
    
    def attack(self, villain):
        print(f"{self.name} swoops down on {villain} from above!")
        self.strength -= 8

flash = Speedster("FlashBolt", strength=90, health=100)
hawk = Flyer("HawkWing", strength=80, health=120)

flash.display_info()
hawk.display_info()
flash.attack("Dr. Doom")
hawk.attack("Dark Shadow")


