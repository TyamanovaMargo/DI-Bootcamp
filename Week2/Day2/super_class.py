#super() автоматически находит следующий класс в иерархии наследования и вызывает его метод.


# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound) # With the super() function, you can gain access to inherited methods that have been overwritten in a class object.
#         # Or : Animal.__init__(self,type, number_legs, sound)
#         self.fetch_ball = fetch_ball

# porcupain = Animal("porcupine",4,'dedwdedew')


# rex = Dog('dog', 4, "wouaf", True)
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# print('This dog has', rex.number_legs , ' legs')
# # >> This dog has 4 legs

# print('This dog makes the sound ', rex.sound)
# # >> This dog makes the sound wouaf

# print('Does this dog fetchs balls ? ', rex.fetch_ball)
# # >> Does this dog fetchs balls ? True


# class MyClass(object):
#     def func(self):
#         print("I'm being called from the Parent class")


# class ChildClass(MyClass):
#     def func(self):
#         print("I'm actually being called from the Child class")
#         print("But...")
#         # Calling the `func()` method from the Parent class.
#         super(ChildClass, self).func()

# my_instance_2 = ChildClass()
# my_instance_2.func()

'''


We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor 
version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.
'''
class Door:
    def __init__(self, is_opened=False):
        self.is_opened = is_opened

    def open_door(self): #change the state and print messages.
        self.is_opened = True
        print("The door is now open.")

    def close_door(self): #change the state and print messages.
        self.is_opened = False
        print("The door is now closed.")

class BlockedDoor(Door): # Inherits from Door.
    def open_door(self):
        raise RuntimeError("Error: A blocked door cannot be opened.") #o raise an RuntimeError, preventing changes.

    def close_door(self):
        raise RuntimeError("Error: A blocked door cannot be closed.")

# Example Usage:
door = Door()
door.open_door()  # Output: The door is now open.
door.close_door()  # Output: The door is now closed.

blocked_door = BlockedDoor()
blocked_door.open_door()  # Raises RuntimeError: A blocked door cannot be opened.


