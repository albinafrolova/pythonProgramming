class Animal:
    def __init__(self, domestic, eatsGrass,legs):
        self.domestic = domestic
        self.eatsGrass = eatsGrass
        self.legs = legs
    def displayAnimal(self):
        if self.eatsGrass:
            return self.domestic + " has " + str(self.legs) + " legs and eats the grass."
        else:
            return self.domestic + " has " + str(self.legs) + " legs and doesn't eat the grass."

class Mammal:
    def __init__(self, domestic, eatsGrass, legs, milk):
        super().__init__(domestic,eatsGrass,legs)
        self.milk = milk
    def displayMammal(self):
        if self.milk:
            print(super().displayAnimal() + "And drinks milk.")
        else:
            print(super().displayAnimal() + "And doesn't drink milk.")

a1=Mammal("domestic", True, 4, False)
a1.displayMammal()

a2=Mammal("domestic", False, 2, True)
a2.displayMammal()

a3=Mammal("wild", True, 4, False)
