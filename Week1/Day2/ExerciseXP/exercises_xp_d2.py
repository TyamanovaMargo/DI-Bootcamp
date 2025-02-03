#================ 🌟 Exercise 1 : Favorite Numbers =============
'''
    Create a set called my_fav_numbers with all your favorites numbers.
    Add two new numbers to the set.
    Remove the last number.
    Create a set called friend_fav_numbers with your friend’s favorites numbers.
    Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
'''

my_fav_numbers = {23,45,67,8,89,100}

# add two new numbers to the set
my_fav_numbers.add(1000)
my_fav_numbers.add(2000)
print(my_fav_numbers)

#remove the last number
my_fav_numbers.pop()

# create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {45,77,23,13,745}

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)



#================ 🌟 Exercise 2: Tuple =============
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# no, because tuples: immutable( not can be changed)


#================ 🌟 Exercise 3: List =============

'''
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

    Remove “Banana” from the list.
    Remove “Blueberries” from the list.
    Add “Kiwi” to the end of the list.
    Add “Apples” to the beginning of the list.
    Count how many apples are in the basket.
    Empty the basket.
    Print(basket)
'''

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

#Remove “Banana” from the list and “Blueberries” from the list.
basket.remove('Banana')
basket.remove('Blueberries')
print(basket)

# add “Kiwi” to the end of the list
basket.append('Kiwi')


# add “Apples” to the beginning of the list.
basket.insert(0,'Apples')

# count how many apples are in the basket.
amount = basket.count('Apples')

#Empty the basket and print
basket.clear()
print(basket)

# #================ 🌟 Exercise 4: Floats =============
# '''

#     What is a float? What is the difference between an integer and a float?
#     Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#     Can you think of another way to generate a sequence of floats?
# '''

# #float its is a floating-point number ,integer is a whole number without a fractional part
list_of_int_float = []

for i in range (3,11,2): #start,stop,step = 2
    list_of_int_float.append(i) # add 3
    list_of_int_float.append(i + 0.5) #add 3.5
print(list_of_int_float)


# #================ 🌟 Exercise 5: For Loop =============

'''

    Use a for loop to print all numbers from 1 to 20, inclusive.
     Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
 '''
# use a for loop to print all numbers from 1 to 20, inclusive.
# # using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for i,number in enumerate(range (1,21)):
    if i % 2 == 0:
        print(f'Index- {i},Number - {number}')


#================ 🌟 Exercise 6 : While Loop =============

# write a while loop that will continuously ask the user for their name, unless the input is equal to your name
name_of_users = ""
while name_of_users.capitalize() != "Margarita":
     name_of_users = input("What is your name?")
     

================ 🌟 Exercise 7: Favorite fruits =============
'''

    Ask the user to input their favorite fruit(s) (one or several fruits).
    Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
    Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    Now that we have a list of fruits, ask the user to input a name of any fruit.
        If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
        If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
'''


fruits = input("Enter your favorite fruit(s), separated by a space (e.g., 'apple mango cherry'): ")
list_of_fruits = list(fruits.split()) # split for separet word word noot character by character
# print(list_of_fruits)

fav_fruit = input("Enter your favorite fruit: ")

if fav_fruit in list_of_fruits :
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')


================ Exercise 8: Who ordered a pizza ? =============

'''

    Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
    As they enter each topping, print a message saying you’ll add that topping to their pizza.
    Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
'''

topping = ""
list_of_topping = []

while topping != "quit":
        topping = input('Enter a series of pizza toppings: ')
        if topping == "quit":
                break
        else :
            list_of_topping.append(topping)
            total_price = (10 + 2.5 *len(list_of_topping) )        
print(f'you’ll add that topping to their pizza: {list_of_topping} and price will {total_price}')


#================ Exercise 9: Cinemax =============
'''

    A movie theater charges different ticket prices depending on a person’s age.
        if a person is under the age of 3, the ticket is free.
        if they are between 3 and 12, the ticket is $10.
        if they are over the age of 12, the ticket is $15.

    Ask a family the age of each person who wants a ticket.

    Store the total cost of all the family’s tickets and print it out.

    A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
    Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
    At the end, print the final list.
'''

age = (input("How old are you? ")).split(',')

cost_of_tickets_total = 0
list_of_ages = []
list_of_ages = age

for each_age in list_of_ages :
    age = int(each_age)
    if  age <= 3:
     cost_of_tickets_total += 0
    elif 3 < age <= 12:
        cost_of_tickets_total += 10
    elif  age > 12:
        cost_of_tickets_total += 15
print(f'Total cost {cost_of_tickets_total}')



names_of_group = ["Liza","Alina","Kirill","Alex"]
names_of_those_allowed = []

for each_name in names_of_group:
    age = int(input(f"How old are you {each_name}?"))
    if 16 < age < 21:
        print("You are permitted")
        names_of_those_allowed.append(each_name) # add nemes of people who were allowed
    else:
        print("You are not allowed.")
#     At the end, print the final list.
print(f"{names_of_those_allowed} are permitted")
      
      
      
#================ Exercise 10 : Sandwich Orders =============
'''
Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

    The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
    We need to prepare the orders of the clients:
        Create an empty list called finished_sandwiches.
        One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
    After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
'''

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich') #remove "Pastrami sandwich", new list ["Tuna sandwich","Avocado sandwich",  "Egg sandwich", "Chicken sandwich"]
    
print(sandwich_orders)
finished_sandwiches = [] #put here sand 

while sandwich_orders:
    sandwich = sandwich_orders.pop() # remove last one 
    finished_sandwiches.append(sandwich) # removed element add to list finished_sandwiches
for sandwiches in finished_sandwiches:
    print(f"I made your {sandwiches}")