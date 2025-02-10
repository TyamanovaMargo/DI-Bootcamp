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
        # print(f"{self.animals}")      
                 

 
    
    def  get_animal_types (self):
        sorted_animals = sorted(self.animals)
        return sorted_animals

    def get_short_info(self,):
        animals  =  self.get_animal_types()
        print(animals)
        if len(animals) == 1:
            output  = animals[0]
        elif len(animals) == 2:
            output = " and ".join(animals)
        else:
            output = ",".join(animals[:-1])
        
        print(f"McDonald’s farm has {output}")

       
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
# macdonald.get_animal_types()
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
macdonald.get_short_info()