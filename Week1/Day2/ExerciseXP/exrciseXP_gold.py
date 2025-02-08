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

alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        print("Vowel")
    else:
        print("Consonant")
