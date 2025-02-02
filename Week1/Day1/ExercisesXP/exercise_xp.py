#======== Exercise 1 ============

print("Hello World \n"* 5)

#======== Exercise 2 ============

print(99 ** 3 * 8)

#======== Exercise 3 ============

# (5 < 3) False
# (3 == 3) True
# (3 == "3") False
# ("3" > 3) Error
# "Hello" == "hello") False

#======== Exercise 4 ============

computer_brand = "Apple"
print(f'I have a {computer_brand} computer')

#======== Exercise 5 ============

name = "Margo"
age = 29
shoe_size = 37
info = f"Hey! My name {name}.I've been learning Japanese almost 10 years. Now I'm {age} and my shoe size is {shoe_size}"
print(info)

#======== Exercise 6 ============
a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))
if a > b :
    print('Hello World')
else :
    print(f'{a} is not bigger then {b}')

#======== Exercise 7 =================
number_from_user = int(input("Enter a number a : "))

if number_from_user % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

#======== Exercise 8 =================

my_name = "Margo" 
user_name = input("What's your name? ")

if user_name.lower() == my_name.lower():
    print("No way! One of us is the clone... ")
else:
    print(f"{user_name}? Cool name")

#======== Exercise 9 =================

height_of_user = int(input("How tall are you (in cm)? "))

if height_of_user > 145 :
    print("tall enough to ride")
else:
    print("need to grow some more to ride")