#============= 🌟 Exercise 1 : Pets    ================
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

    
# '''

#     Create another cat breed named Siamese which inherits from the Cat class.
#     Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
#     Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
#     Take all the cats for a walk, use the walk method.

    
# '''
# bengal = Bengal("Bo",2)
# chartreux = Chartreux("Gor",7)
# siamese = Siamese("Pinky",6)
# all_cats = [bengal,chartreux,siamese]
# print(all_cats)

# sara_pets = Pets(all_cats)
# sara_pets.walk()


#================= 🌟 Exercise 2 : Dogs ==============

class Dog :
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return print(f"{self.name} is barking")
    
    def running_speed(self):
        return int((self.weight/self.age * 10))
    
    def fight(self,other_dog):
        combat_ability_our_dog = self.running_speed() * self.weight
        combat_ability_other_dog = other_dog.running_speed() * other_dog.weight
        if combat_ability_our_dog > combat_ability_other_dog:
             return print(f"Winner is {self.name}")
        else:
            return print(f"Winner is {other_dog.name}")


BorderCollie = Dog("Luna",5,20)

GoldenRetriever = Dog("Max",6,26)

FrenchBulldog = Dog("Charlie",3,10)

BorderCollie.bark()
GoldenRetriever.bark()
FrenchBulldog.bark()

BorderCollie.running_speed()
GoldenRetriever.running_speed()
FrenchBulldog.running_speed()

BorderCollie.fight(GoldenRetriever)
GoldenRetriever.fight(FrenchBulldog)
BorderCollie.fight(FrenchBulldog)





#=============== Exercise 4 : Family =======================

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members


    def born(self, **kwargs):
        print(f"Congrats! A new child, {kwargs['name']}, has been born.")
        self.members.append(kwargs)

    def is_18(self, member_name):
        for member in self.members:
            if member["name"] == member_name:
                return member["age"] >= 18
        return False 

    def family_presentation(self):
        print(f"{self.last_name} family details")
        for member in self.members:
            for key,val in member.items():
                print(f"{key} : {member[val]}")



family_members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]


burov_family = Family(family_members, "burov")

burov_family.born(name="Sarah", age=3, gender="Female", is_child=True)
burov_family.family_presentation()


print(f"Is Michael over 18? {burov_family.is_18('Michael')}")
print(f"Is Sarah over 18? {burov_family.is_18('Emily')}")


#======== Exercise 5 : TheIncredibles Family ===================
'''


Create a class called TheIncredibles. This class should inherit from the Family class:
This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

Add a method called incredible_presentation which :

    Print a sentence like “*Here is our powerful family **”
    Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
'''

class TheIncredibles(Family):
    def use_power (self,member_name):
        # if self.is_18 == False:
        #     (f"{self.name} is not over 18 years old and cannot use power.")
        # else:
        #     print(f"{self.name} uses their power: {self.power}!")
      def use_power(self, member_name):
    # Find the family member
        for member in self.members:
            if member["name"] == member_name:
                # if member["age"] < 18:
                if self.is_18() == False:
                    print(f"{member_name} cannot use their power because they are under 18.")
                    return
                print(f"{member_name} uses their power: {member['power']}!")
                return
        print(f"{member_name} is not found in the family.")



    def incredible_presentation(self):
        print(" Here is our power family ")
        super().family_presentation() #function in Python allows a subclass to access methods from its parent (superclass)

incredible_family_members =   [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]
incredibles = TheIncredibles(incredible_family_members, "Incredibles")
incredibles.use_power("Michael")

incredibles.incredible_presentation()
incredibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")
incredibles.incredible_presentation()