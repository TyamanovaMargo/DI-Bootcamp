class Farm :
    
    def __init__(self,name,animals): #When an object is created, python automatically runs the __init__() (it has to be called that) method of the class.this method must have at least one argument, self
        self.name = name
        self.animals = list(animals)    #attributes
        print(f"{name}'s farm ")

    def add_animal(self, animal, count = 0):
        self.animals.append(animal)
        print(self.animals)

    def get_info():
        pass  

    








macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
# print(macdonald.get_info())