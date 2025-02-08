# # ordered and mutable
# # ++++ List can’t be a dictionary key.!!!!+++++++++++++
# user_info = {'name':'Ron',  # key smth immutable
#              'last_name' : "Weasley",
#              'age': 17,
#              'adress' : "Ottery Village",
#              'family' : [('Arthur','Father',50),('Molly','Mother',48)],
#              'hobbies' : {'Quiditch','Swimming'},
      
#              }

# # user_info2 = {'name':'Harry',  # key smth immutable
# #              'last_name' : "Potter",
# #              'age': 17,
# #              }

# # print(user_info["name"]) # we enter key's name 
# # print(user_info["family"][0])

# # exercise
# # sample_dict = { 
# #    "class":{ 
# #       "student":{ 
# #          "name":"Mike",
# #          "marks":{ 
# #             "physics":70,
# #             "history":80
# #          }
# #       }
# #    }
# # }

# # print(sample_dict["class"]["student"]["marks"]["history"])

# # ids_dict = { 0: 123,
# #             1:456,
# #             2 : 678
# #             }

# # #modify an entry
# # user_info["age"] = 18
# # print(user_info)

# # #adding a new entry
# # user_info['School'] = "Hoqwarts"
# # print(user_info)

# # # deleting an entry
# # del user_info['School']
# # print(user_info)

# # print('hobbies' in user_info) # to check key yes or not

# # if 'age' in user_info :
# #     print(user_info['age'])
# # else: 
# #     print("this key doesn't exist")

# # # how work for 
# # for relative in user_info['family']:
# #     print (relative)

# # exercise 2

# student_info = {
#     'name': 'John',
#     'age': 25,
#     'hobbies': ['reading', 'gaming', 'cycling'],
#     'city': 'New York'
# }

# # Tasks:
# # 1 - Change the value of 'age' from 25 to 30.
# # student_info['age'] = 30
# # print(student_info)
# # # 2 - Add a new entry with the key 'occupation' and the value 'Engineer'.
# # student_info['occupation'] = 'Engineer'
# # print(student_info)
# # # 3 - Remove the entry with the key 'city'.
# # del student_info['city']
# # print(student_info)
# # # 4 - check if the key 'email' is on the dictionary, if not, add it with value 'name@gmail.com'
# # if 'email' not in  student_info:
# #     student_info['email'] = 'name@gmail.com'
# # print(student_info)
# # # 5 -Loop through the values in the 'hobbies' list and print each hobby on a new line.
# # for item in student_info['hobbies']:
# #     print(item)

# # print(user_info.keys())
# # print(type(user_info.values()))

# # for value in user_info.values():
# #     print(value)

# # for key, value in user_info.items():
# #     if key == 'age':
# #         user_info['age'] += 5
# #     print(key,value)

# # print(user_info)

# # exerise 3

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]

# #{'city': 'New york', 'age': 25}

# for item in keys_to_remove:
#     if  item in sample_dict.keys() :
#         del sample_dict[item] 
# print(sample_dict)

# car = { 'color': 'red',
#        'brand': "bmw",
#        'year': 1990
# }
# car.update({"model": "mazda",
#             'owner': "jonh",
#             "has ensurance": True})
# print(car)

# ZIP = Very useful built in method

names = ['Lea','Dart Vaider','Luke','Chubacca']
power = [150,500,489,100]

star_wars = dict(zip(names, power))
print(star_wars)



for  char_name  in names:
    if char_name == 'Dart Vaider':
        continue
    print(char_name)