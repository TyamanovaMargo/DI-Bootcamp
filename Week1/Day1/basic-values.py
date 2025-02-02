# BASIC VALUE TYPES

# print('hello world') # string sequence of chars

# print(8 + 2) # numbers: 2 options -integer (not decimal), float (decimal numbers)
# print(type(5.35))
# print(type(10))
# print(type('`hello'))

# exercise 1 discover and print type of the following values:

# values =[5,2.54,'Good Morning']
# print (type(values)) # list

# for value in values:
#     print(type(value))

# print(5 < 7)
# print (5 > 7)
# print('5' == 5)

# string = sequence of char. So I can use indexing

# name = "juliana schmidt "
# print(name[3])
# print(name[3:7])
# print(name[4:7])

# len() = dicover the length of the string
# print(len('Harry Potter'))
# print(name[4:len(name)])
# print(name[4:])
# print(name[:])

# exercise 2
# name = "margarita"
# print(name[4])
# print(name[1])
# print(name [6:len(name)])

# print(name.capitalize())
# print(name.title())
# print(name.lower())

# my_hp_name = name.replace("schmidt","Granger")
# print(my_hp_name)

# user_name = '!Jonh Doe!'
# cleaned_user_name = user_name.strip('!') # to delete something for cleaning
# print(cleaned_user_name)

#numbers

# print(4 + 3)
# print(4 - 3)
# print(4 ** 3)
# print(4 * 3)
# print(4 / 2)
# print(5 % 2)

# name = 'ju'
# name += 'u'
# print(name)

# user_age = input('What is your age?')
# my_height = '1.68'
# # print(user_age)
# user_height_float = float(my_height)
# print(user_height_float)
# #type Casting (changing the type of value)
# user_age_int = int(user_age)
# print(user_age_int + 7)


# print('hello world' * 4, sep = '')

first_name = 'Margarita'
last_name = 'Tyamanova'
print(f'My full name {first_name},{last_name}', sep = " ")