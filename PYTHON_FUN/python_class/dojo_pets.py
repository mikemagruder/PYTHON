
class Pet:
    def __init__(self, name , type , tricks , noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health =+ 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)
        

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    #     # walk() - walks the ninja's pet invoking the pet play() method
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self
    #     # feed() - feeds the ninja's pet invoking the pet eat() method
    def bathe(self):
        self.pet.noise()
    #     # bathe() - cleans the ninja's pet invoking the pet noise() method

my_treats = ['chicken','hot dogs',"nibbles"]
my_pet_food = ['rice','chicken']

fido = Pet("fido", "dog", [ "runs", "eats everything"] , "woof!")


mike = Ninja("Mike", "Magruder", my_treats, my_pet_food, fido)

mike.feed();
mike.feed();
mike.feed();

# print(mike.first_name)
# print(mike.last_name)
# print(mike.treats)
# print(mike.pet_food)
# print(mike.pet)
# print(mike.pet.name)
# print(mike.pet.type)
# print(mike.pet.tricks)
# print(mike.pet.health)