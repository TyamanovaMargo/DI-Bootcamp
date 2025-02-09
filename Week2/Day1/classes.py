# class Dog:
#     def __init__(self, color, breed, floppy_ears):
#         print("A new dog has been initialized")
#         self.color = color
#         self.breed = breed
#         self.floppy_ears = floppy_ears

#     def __str__(self):  # Fix the method name (double underscores)
#         return f"{self.breed}, {self.color}, {self.floppy_ears}"
#     def bark(self):
#         return f"{self.name}' goes WOOF"
    
#     def fetch(self,object):

# Example usage:
# buba = Dog("brown", "Chaani", True)
# dingo = Dog("dingo","white",'chaani')

# print(buba) 
# print(dingo)  # Now prints: Labrador, brown, True


class Book : 
    def __init__(self,title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.checked_out = False

    def checkedOut(self):
        if self.checked_out == True:
            print("Is already cheked out")
        else:
            self.checked_out = True
            print(f"Your code {self.title} is sucseful")

    def check_in(self):
        self.checked_out = False


moby_dick = Book("Mobe Dick","Herman Melvile", 1851)
moby_dick.checked_out()