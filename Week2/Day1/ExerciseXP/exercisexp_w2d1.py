#============== 🌟 Exercise 1: Cats ===================

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        
# Instantiate three Cat objects using the code provided above.       
# cat1 = Cat("Lusya",18)
# cat2 = Cat("Bonya",6)
# cat3 = Cat("Nora",13)

# # a function that finds the oldest cat and returns the cat.
# def oldest_age_cat ( * args):
#     oldest_cat = args[0] # cat1 = Cat("Lusya",18)
    
#     for cat in args[1:]:  #args from position 1
#         if cat.age >= oldest_cat.age:
#             oldest_cat = cat #each cat our object belongs to Cat

#     # print(f'The oldest cat is {cat.name}, and is {cat.age} years old.')
#     return print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')

   
# #call func
# oldest_cat = oldest_age_cat ( cat1,cat2,cat3)

#======================= 🌟 Exercise 2 : Dogs ======================

#Create a class called Dog.
# class Dog : 
#     def __init__(self, name, height):  #in this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
#         self.name = name
#         self.height = height
#         print(f'Name is {name} and height is {height}')
    
#     def bark(self):
#         print(f"{self.name} goes woof!")
#     def jump(self):
#         x = self.height *2
#         print(f"{self.name} jumps {x} cm hight!")

# # my_dog = Dog("Buba",90)
# # my_dog.bark()
# # my_dog.jump()

# davids_dog = Dog("Rex",50)
# davids_dog.jump()
# davids_dog.bark()

# sarahs_dog = Dog("Teacup",20)
# sarahs_dog.jump()
# sarahs_dog.bark()
                 
# biggest_dog = davids_dog
# if sarahs_dog.height > biggest_dog.height:
#     biggest_dog = sarahs_dog
# print(f"{biggest_dog.name} of the bigger dog")

#============== 🌟 Exercise 3 : Who’s the song producer? ===========
'''
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

'''
# class Song():
#     def __init__(self,lyrics = []):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for each_element in self.lyrics:
#             print(each_element)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#============== Exercise 4 : Afternoon at the Zoo ===============
'''
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter. 
'''

class Zoo():
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.list_animals = []
    
    def add_animal(self, new_animal): #add animal to the list
            while new_animal not in self.list_animals:
                self.list_animals.append(new_animal)
                print(f"{new_animal} added")
                # print(self.list_animals)
            
    def get_animals(self): #prints all the animals of the zoo.
        for animal in self.list_animals:
            print(animal)

    def sell_animal (self,animal_sold): #his method removes the animal from the list and of course the animal needs to exist in the list.
        self.list_animals.remove(animal_sold)
        # print(self.list_animals)

    def sort_animals(self): #sorts the animals alphabetically and groups them together based on their first letter. 
        sorted_animals = sorted(self.list_animals)
        # print(f"Sorted list of animals {sorted_animals}")
        dict_animals ={ }
        for animal in sorted_animals:
            print(animal[0]) #take first char
    
    
    
    def get_groups (self): #prints the animal/animals inside each group.
        pass


# def ramat_gan_safari(): #call all the methods.
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Lion")
# ramat_gan_safari.add_animal("Elephant")
# ramat_gan_safari.add_animal("Cheetos")
# ramat_gan_safari.add_animal("Emu")
# ramat_gan_safari.get_animals()
# ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.sort_animals()

    
