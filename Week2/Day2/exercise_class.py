# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")
# class Dog(Animal):
#     pass
# class Giraffe(Animal):
#     def eat_leaf(self):
#         print("I eat a leaf that's high un the tree")
# # dingo = Dog("Dingo")

# # print(dingo.name)
# # dingo.bark()
# dingo = Dog('dog',4,'Woof')
# dingo.make_sound()
# joshua = Giraffe('Giraffe',4,"sffdfdfdf")

# joshua.make_sound()
# joshua.eat_leaf()

# dingo.eat_leaf() # it doesnt work

# blob_fish = Animal("fish",0,"blup blup")
# blob_fish.eat_leaf()
# blob_fish.make_sound()

class Circle:
    color ="red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle 
print(nc.color)

# >> What will be the output ? blue

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)

nc.grow() #1 * 2 * 2

print(nc.diameter)
# >> What will be the output - 4!



