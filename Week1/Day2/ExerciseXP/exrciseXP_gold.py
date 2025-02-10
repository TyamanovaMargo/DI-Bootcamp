# ======= Exercise 1: Concatenate lists ======
# Write code that concatenates two lists together without using the + sign.

# list1 = [23,45,6,75]
# list2 = [56, 784, 89]
# list1.extend(list2)
# print(list1)

#==========Exercise 2: Range of numbers ======
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# for i in range(1500,2500):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)


#========== Exercise 3: Check the index ======
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# # # Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name
# users_name = input("What is it you name ?")


# for i,name in enumerate(names) :
#     if users_name.capitalize() == name:
#         print(f"if input is {users_name} we should be printing the index {i}")
#         break
#     else:
#         print(f"Sorry,{users_name} not in the list")
    
   

#========== Exercise 4: Greatest Number ===============

#Ask the user for 3 numbers and print the greatest number.
# number1 = int(input("Input the 1st number: "))
# number2 = int(input("Input the 1st number: "))
# number3 = int(input("Input the 1st number: "))



#================== Exercise 5: The Alphabet ============

'''
    Create a string of all the letters in the alphabet
    Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
'''

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in alphabet:
#     if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
#         print("Vowel")
#     else:
#         print("Consonant")
#     for i in alphabet :
#         if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
#             print(f"{i} vowel")
#         print(f"{i} Consonant")


'''
Exercise 6: Words and letters
Instructions

    Ask a user for 7 words, store them in a list named words.
    Ask the user for a single character, store it in a variable called letter.
    Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
    If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

'''

# words = [] #creat list
# # for _ in range (7):
# #     words.append(input("Enter 7 words: "))
# words.append(input("Enter 7 words: "))
# letter = input(("Enter a single character: "))

# for word in words:
#     if letter in word:
#         print(f'In word {word} the letter {letter} first appearnce in {word.index(letter)}')
#         break
#     else :
#         print("letter doesn’t exist")
        


#ocean, flame, forest, mirror, stone, echo, whisper



'''
Exercise 7: Min, Max, Sum
Instructions

Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million.
Use the sum() function to see how quickly Python can add a million numbers.
'''

'''
Exercise 8 : List and Tuple
Instructions

Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

'''
Exercise 9 : Random number
Instructions

    Ask the user to input a number from 1 to 9 (including).
    Get a random number between 1 and 9. Hint: random module.
    If the user guesses the correct number print a message that says Winner.
    If the user guesses the wrong number print a message that says better luck next time.
    Bonus: use a loop that allows the user to keep guessing until they want to quit.
    Bonus 2: on exiting the loop tally up and display total games won and lost.
'''