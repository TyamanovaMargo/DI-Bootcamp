class Farm :
    
    def __init__(self,name): #When an object is created, python automatically runs the __init__() (it has to be called that) method of the class.this method must have at least one argument, self
        self.name = name
        self.animals = {}   #attributes
        print(f"{name}'s farm ")

    def add_animal(self, animal,count = 1):
            # while animal not in self.animals:
            #     self.animals.append(animal)
            #     print(f"{animal} added {}")    
        if animal in  self.animals:
                self.animals[animal] += count # to existing count
        else: 
             self.animals[animal] = count
        print(f"{self.animals}")      
                 

    def get_info():
        pass  

    








macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())