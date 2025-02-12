'''

The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

    Compute the circle’s area
    Print the attributes of the circle - use a dunder method
    Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
    Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    Be able to put them in a list and sort them
    Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

'''
import turtle as t

class Circle:
    def __init__(self,radius ):
        self.radius = radius
        

    @property    
    def getRadius(self):
        print(self.radius)

    @property
    def getDiameter(self):
        return 2 * self.radius
    
    @property # it allows call lika an attrib not a func
    def circle_area(self):
        # pi_number = 3.14159 
        return 3.14159 * self.radius **2
    
    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.getDiameter}, area: {self.circle_area:.2f}"
    
    def __lt__(self,other): #Be able to compare two circles to see which is bigger, and return a Boolean
        return self.radius < other.radius

    def __eq__(self, other): #Be able to compare two circles and see if there are equal, and return a Boolean
        return self.radius == other.radius
    
    def __add__(self,other): #Be able to add two circles together, and return a new circle with the new radius
        return Circle(self.radius + other.radius)

circles_list = []
while True:
    input_rad = input('Give me a radius of new crcle :')
    # circle2 = Circle(10,16)

    if  input_rad.lower() == "exit":
        break
    else:
        circle = Circle(int(input_rad))
        circles_list.append(circle)

sorted_list = sorted(circles_list)
for i in sorted_list:
    # print(type(i.radius))

    t.penup()  #will lift the turtle off the “digital canvas” and if you move the turtle in penup state it won’t draw
    t.goto(0, -i.radius)  # Move the turtle so the circle is centered
    t.pendown()#is the default state of turtle
    t.circle(i.radius)  # Draw circle

    # circle3 = Circle(2)3
    # circle.circle_area
    # print(circle)
    # print( circle  < circle2 )  
    # print( circle2 < circle) 
    # print(circle  == circle3)
    # print(circle.__add__(circle3))


