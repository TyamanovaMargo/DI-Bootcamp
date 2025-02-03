# #================ 🌟 Exercise 1 : Favorite Numbers =============
# '''
#     Create a set called my_fav_numbers with all your favorites numbers.
#     Add two new numbers to the set.
#     Remove the last number.
#     Create a set called friend_fav_numbers with your friend’s favorites numbers.
#     Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# '''

# my_fav_numbers = {23,45,67,8,89,100}

# # add two new numbers to the set
# my_fav_numbers.add(1000)
# my_fav_numbers.add(2000)
# print(my_fav_numbers)

# #remove the last number
# my_fav_numbers.pop()

# # create a set called friend_fav_numbers with your friend’s favorites numbers.
# friend_fav_numbers = {45,77,23,13,745}

# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)



# #================ 🌟 Exercise 2: Tuple =============
# # Given a tuple which value is integers, is it possible to add more integers to the tuple?

# # no, because tuples: immutable( not can be changed)


# #================ 🌟 Exercise 3: List =============

# '''
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#     Remove “Banana” from the list.
#     Remove “Blueberries” from the list.
#     Add “Kiwi” to the end of the list.
#     Add “Apples” to the beginning of the list.
#     Count how many apples are in the basket.
#     Empty the basket.
#     Print(basket)
# '''

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# #Remove “Banana” from the list and “Blueberries” from the list.
# basket.remove('Banana')
# basket.remove('Blueberries')
# print(basket)

# # add “Kiwi” to the end of the list
# basket.append('Kiwi')


# # add “Apples” to the beginning of the list.
# basket.insert(0,'Apples')

# # count how many apples are in the basket.
# amount = basket.count('Apples')

# #Empty the basket and print
# basket.clear()
# print(basket)

# #================ 🌟 Exercise 4: Floats =============
# '''

#     What is a float? What is the difference between an integer and a float?
#     Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#     Can you think of another way to generate a sequence of floats?
# '''

# #float its is a floating-point number ,integer is a whole number without a fractional part
# list_of_numbers = [4,2.5,4.5,3,2,3.5,1.5,1]


#================ 🌟 Exercise 5: For Loop =============

'''

    Use a for loop to print all numbers from 1 to 20, inclusive.
    Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
'''
# use a for loop to print all numbers from 1 to 20, inclusive.
for i,b in enumerate(range (1,21)):
    print(f'Index- {i},Number - {b}')

# using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

#================ 🌟 Exercise 6 : While Loop =============

# write a while loop that will continuously ask the user for their name, unless the input is equal to your name

name_of_users = ""
while name_of_users.capitalize != "Margarita":
     name_of_users = input("What is your name?")
     if name_of_users.capitalize == "Margarita":
          break
