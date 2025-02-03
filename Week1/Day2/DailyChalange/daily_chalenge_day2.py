# #================= Challenge 1 =======================
number_from_users = int(input("Enter a number: "))
length = int(input("Enter the length: "))

list_of_numbers_mult = []
for i in range(1, length + 1): #lentgh +1 inclusive lenght
    list_of_numbers_mult.append(number_from_users * i) # get the multiple.

print(list_of_numbers_mult)



#================= Challenge 2 =======================

#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
string_from_user = input("Give me a string: ")
list_of_mod_string = []
string_joined = ''

for char in string_from_user:
    if char not in list_of_mod_string:
        list_of_mod_string.append(char) # in this stage they splite char by char
print(string_joined.join(list_of_mod_string))