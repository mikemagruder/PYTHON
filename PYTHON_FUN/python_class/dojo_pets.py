
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
        print(f"{self.name} is sleeping...zzzzz!")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        if self.energy < 30:
            print(f"Time for {self.name} to rest!")
        else:
            print(f"Keep playing!")
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

print(f"{mike.pet.name}'s BIG adventure!")
mike.feed()
mike.feed()
mike.feed()
mike.pet.play()
mike.pet.play()
mike.pet.play()
mike.pet.play()
mike.pet.sleep()
mike.pet.sleep()
print(mike.pet.noise)
print(f"{mike.pet.name}'s final energy score: {mike.pet.energy}")
print(f"{mike.pet.name}'s final health score: {mike.pet.health}")