#Todo: make text output prettier

class Food:
    name = ""
    cals = 0
    fat = 0
    carb = 0
    prot = 0
    mass = 1

    def __str__(self):
        outputstr = (self.name + ". Cals: " + str(self.cals) + ", fat: " + str(self.fat) + 
                "g, carb: " +  str(self.carb) + "g, prot: "+ str(self.prot) + "g, total mass: " + 
                str(self.mass) + "g")

        return outputstr

    def __add__(self, other):
        newfood = Food()
        newfood.name = self.name + "+" + other.name
        newfood.cals = self.cals + other.cals
        newfood.fat = self.fat + other.fat
        newfood.carb = self.carb + other.carb
        newfood.prot = self.prot + other.prot
        newfood.mass = self.mass + other.mass
        return newfood

    def __rmul__(self, c):
        newfood = Food()
        newfood.name = str(c) + "*" + self.name
        newfood.cals = c * self.cals
        newfood.fat = c * self.fat
        newfood.carb = c * self.carb
        newfood.prot = c * self.prot
        newfood.mass = c * self.mass
        return newfood

class Wholemilk(Food):
    def __init__(self):
        self.name = "Whole milk"
        self.cals= 0.61
        self.fat= 0.032
        self.carb=0.048
        self.prot= 0.032

class Quickoats(Food):
    def __init__(self):
        self.name = "Quick oats"
        self.cals= 0.68
        self.fat= 0.014
        self.carb=0.12
        self.prot= 0.024

class Cocoapowder(Food):
    def __init__(self):
        self.name = "Cocoa powder"
        self.cals= 4.0
        self.fat= 0.2
        self.carb= 0.4
        self.prot= 0.2

class Rawhoney(Food):
    def __init__(self):
        self.name = "Raw honey"
        self.cals= 3.04
        self.fat= 0.0
        self.carb= 0.82
        self.prot= 0.003

class Blackberries(Food):
    def __init__(self):
        self.name = "Blackberries"
        self.cals= 0.43
        self.fat= 0.005
        self.carb= 0.1
        self.prot= 0.014

class Crunchypb(Food):
    def __init__(self):
        self.name = "Crunchy peanutbutter"
        self.cals= 200.0/32
        self.fat= 0.5
        self.carb= 6.0/32
        self.prot= 0.25


    
## Want:
#  Enter names and grams. Get total calories and macros. 
#  I could either: store a dictionary of vectors and combine
#  Or: have a Food class and a bunch of data in JSON. On start of program, make a bunch of food obects using JSON data. Then just add food objects and print a table of values...
#  The second way is way sexier, but first way is way more efficient.
#  OR the best way, I think, is to have a separate subclass for each type of food. Then it's like the first way but without messing with JSON


