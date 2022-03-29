#exercise
class Poem: #initialising class
    color = "" #color  is the attributes of the class; and color is a list (data structure)
    feel = "" #feel is the attribute of the class; and the feel is a list (data structure)
rose = Poem() #rose is an object of the class Poem
rose.color = "red" #giving rose object a color attribute that has value of "red"

violet = Poem() #violet is an object of the class Poem
violet.color = "blue" #giving object violet a color attribute that has value of "blue"

thisPunIsForYou = Poem() #printing the class execution

print("Roses are {}, ".format(rose.color))
print("Violet are {}.".format(violet.color))

print(thisPunIsForYou)


#3 OOP 

class City:
    name = ""
    country = ""
    elevation = 0
    population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    return_city = City()

    if city1.population >= min_population:
        return_city = city1

    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2 

    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    if return_city.name:
        return (" {}, {}".format(return_city.name, return_city.country))
    else:
        return ""


print(max_elevation_city(100000))
print(max_elevation_city(1000000))
print(max_elevation_city(10000000))

#5

class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "red"
table.material = "wood"

couch = Furniture()
couch.color = "brown"
couch.material = "leather"

def describe_furniture(piece):
    return("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))
print(describe_furniture(couch))
print(Furniture)


#exercise

class Piglet:
    name = "piglet"
    years = 0
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        return self.years * 18


hamlet = Piglet()
hamlet.speak()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = 'Petunia'
petunia.speak()
hamlet.name = "Ptonia"
hamlet.speak()

piggy =  Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())

#constructor and other special methods

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)


class Apple_1:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor =  flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple_1("red", "sweet")
print(jonagold)


help(Apple_1)


def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds"""
    return hours*3600 + minutes*60 + seconds

help(to_seconds)


#code reuse and inheritance

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith =  Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor, carnelian.flavor)


class Animals:
    sound = ""
    def __init__(self, name): #special method of a class
        self.name = name
    def speak(self): #method of class
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animals):
    sound = "Oink!"

smally = Piglet("Small Piggy") #creatign an instance of a class

class Cow(Animals):
    sound = "Mooo"

milky = Cow("Milky White")
milky.speak()
smally.speak()

#exercise
class Repository:
    def __init__(self): #special method
        self.packages = {}
    def add_package(self, package): #adding package method
        self.packages[package.name] = package
    def total_size(self): #calculating size method
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

#exercise

class Clothing:
    stock = { "name": [], "material": [], "amount": []}
    def __init__(self, name): #constructor method
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock["name"].append(self.name)
        Clothing.stock["material"].append(self.material)
        Clothing.stock["amount"].append(amount)
    def stock_by_material(self, material):
        count = 0
        n = 0

        for item in Clothing.stock["material"]:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count

class Shirt(Clothing):
    material = 'cotton'
class Pants(Clothing):
    material = 'cotton'


polo =  Shirt("Polo")
sweatpants = Pants("Sweatpants")

polo.add_item(polo.name, polo.material, 15)
sweatpants.add_item(sweatpants.name, sweatpants.material, 89)
current_stocks = polo.stock_by_material("cotton")
print(current_stocks)

#python modules 

from collections import namedtuple
import random

from module4GradedAssessment import carListing
print(random.randint(1, 10))
import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now + datetime.timedelta(days=58))
print(now.month)

 
#exercises of inheritance & composition

class Animal:
    name = ""
    category = ""
    def __init__(self, name):
        self.name = name 
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if category == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle('Turtle')
snake = Snake("Snake")

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))




