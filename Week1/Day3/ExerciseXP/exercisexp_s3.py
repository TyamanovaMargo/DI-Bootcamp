#========== 🌟 Exercise 1 : Convert lists into dictionaries ==========
'''
Convert the two following lists, into dictionaries.
Hint: Use the zip method
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)


#========== 🌟 🌟 Exercise 2 : Cinemax #2 ==========
'''
    A movie theater charges different ticket prices depending on a person’s age.

    if a person is under the age of 3, the ticket is free.
    if they are between 3 and 12, the ticket is $10.
    if they are over the age of 12, the ticket is $15.
'''

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
new_person = input("Give me a name: ")
new_age = int(input("Give me an age: "))


cost_for_each = {}
total_cost = 0


family[new_person] = new_age
for name,age in family.items():
    if  age <= 3:
        ticket_cost = 0
    elif 3 < age <= 12:
        ticket_cost = 10
    elif  age > 12:
        ticket_cost = 15
# Print out the family’s total cost for the movies.
    cost_for_each[name] = ticket_cost
    total_cost += ticket_cost
print(f'Have to pay each {cost_for_each} and total price{total_cost}')
   
#========== 🌟 Exercise 3: Zara ==========
#Create a dictionary called brand which value is the information from part one (turn the info into keys and values). 

brand = { "name": "Zara",
         "creation_date": 1975, 
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes":['men', "women", "children", "home"],
         "international_competitors" : ["Gap", "H&M", "Benetton"],
         "number_stores": 7000 ,
         "major_color":{"France": "blue", 
                        "Spain": "red", 
                        "US": ["pink", "green"]}
}

# Change the number of stores to 2.
brand["number_stores"] = 2
print(brand)

#Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are
clients = ",".join(brand["type_of_clothes"])
# print(type(clients)) #str
print(f'Zaras clients are: {clients}')

# Add a key called country_creation with a value of Spain
brand["country_creation"] = "Spain"
print(brand)

#Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand.keys():
    brand["international_competitors"].append('Desigual')  #adding new data to existing key-value pairs
# print(brand["international_competitors"])

# Delete the information about the date of creation.
del brand["creation_date"]
# print(brand)

# Print the last international competitor
print(brand["international_competitors"][-1])

#Print the major clothes colors in the US
color_in_us = ",".join(brand["major_color"]['US'])
print(color_in_us)

#Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))


#Print the keys of the dictionary.
print(brand.keys())



#Create another dictionary called more_on_zara with the following details:
'''
    creation_date: 1975 
    number_stores: 10 000
'''
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
#Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)


#Print the value of the key number_stores. What just happened ?
print(brand['number_stores']) #10000 updated

#======= Exercise 4 : Disney characters ========

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

numbers  = [0,1,2,3,4]

disney_users_A = dict(zip(users,numbers))
print(disney_users_A)

disney_users_B = dict(zip(numbers,users))
print(disney_users_B)

disney_users_C = dict(sorted(disney_users_A.items()))
print(disney_users_C)

contain_special_char_user ={}
for i, name in enumerate(users):
    if "i" in name:
        contain_special_char_user[name] = i
print(contain_special_char_user)

spacial_user = {}
for i, name in enumerate(users):
    if name.startswith("M") or name.startswith("P"):
        spacial_user[name] = i
print(spacial_user)