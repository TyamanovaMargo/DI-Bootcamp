#Exercise 1: Birthday Look-up

#Create a variable called birthdays. Its value should be a dictionary.
birthday = {}
# print(type(birthday))

#Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
keys = ['Alina Parinova', 'Liza Volkova', 'Olesya Astafurova',' Daniil Nikonov','Gennady Kogan']
values = ["1995/06/12", "1988/09/25", "2000/01/15","1993/04/30","1985/12/05"]

for k, v in zip(keys, values):
    birthday[k] = v

# print(birthday)  

'''
Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“

    Ask the user to give you a person’s name and store the answer in a variable.
    Get the birthday of the name provided by the user.
    Print out the birthday with a nicely-formatted message.

'''

# print("You can look up the birthdays of the people in the list!")
# nameFromUser = input("give me your person’s name")

# if nameFromUser in birthday:
#     print(birthday[nameFromUser])


#Exercise 2: Birthdays Advanced
# print(birthday)
# nameFromUser = input("give me your person’s name")
# if nameFromUser in birthday:
#     print(birthday[nameFromUser])
# else:
#     print(f"Sorry, we don’t have the birthday information for <nameFromUser>")


#Exercise 3: Add Your Own Birthday
# nameFromUser = input("give me your person’s name")
# dateOfBirthday = input("give me your person’s date")
# birthday[nameFromUser] = dateOfBirthday
# print(birthday)


#Exercise 4: Fruit Shop
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# for k,v in items.items() :
#     print(f"Fruit is{k} and price is {v}")

#Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = sum(v["price"] * v["stock"] for v in items.values())

print(f"Total cost is : {total_cost}")