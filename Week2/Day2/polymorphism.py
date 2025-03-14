class Parrot():

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
# >> Parrot can fly

flying_test(peggy)
# >> Penguin can't fly


# Multiple Inheritance

class Alien():
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal():
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")

class AlienDog(Alien, Dog):
    def bark(self):
        print(f"{self.name} barked, 0ul10ul0u (that's how aliens dogs bark..) !")
                                                                   


my_normal_dog = Dog("Roger")
my_normal_dog.sleep()
# >> zzzZZZZZ

my_normal_dog.bark()
# >> Roger barked, WAF !

my_alien_dog = AlienDog("Rex", "Neptune")
print(my_alien_dog.planet)
# >> Neptune

my_alien_dog.fly()
# >> Rex is flying!

my_alien_dog.sleep()
# >> Aliens don't sleep

my_alien_dog.bark()
# >> Rex barked, 0ul10ul0u (that's how aliens dogs bark..) !


# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis() 

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price) # SE
    print(foundation.bored) #False
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored) # True