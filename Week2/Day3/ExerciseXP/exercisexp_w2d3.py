#=========== 🌟 Exercise 1: Currencies #########

'''

    Using the code above, implement the relevant methods and dunder methods which will output the results below.
    Hint : When adding 2 currencies which don’t share the same label you should raise an error.

>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollars'

>>> int(c1)
5

>>> repr(c1)
'5 dollars'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1 
5 dollars

>>> c1 += 5
>>> c1
10 dollars

>>> c1 += c2
>>> c1
20 dollars

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>
'''


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
       return f'{self.amount} {self.currency}'
    
    def __repr__(self):
        return str(self)
    
    def __int__(self):
        return self.amount

    def __add__(self,other):
        return (Currency(self.currency + self.amount + other))

    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# print(str(c1))
# int(c1)
# print (c1 + 5)


#================ 🌟 Exercise 2: Import ======================

'''
Instructions

    In a file named func.py create a function that sum 2 numbers, and prints the result
    In a file named exercise_one.py import the function and call it to print the result

Hint: You can use the the following syntaxes:

import module_name 

OR 

from module_name import function_name 

OR 

from module_name import function_name as fn 

OR

import module_name as mn


'''

#============ 🌟 Exercise 3: String module =================

# import random

# import string

# lenght = 5
# random_string = (" ".join(random.choices(string.ascii_letters,k = lenght))) # string.ascii_letters includes both uppercase and lowercase alphabets.
# print(random_string)


#============ 🌟 Exercise 4 : Current Date =================

from datetime import datetime

# x = datetime.datetime.now()
# print(x) 

#=============== Exercise 5 : Amount of time left until January 1st===============

# def left_until_January():
#     specific_year = 2026
#     first_january = datetime(specific_year, 1, 1)
#     current_date = datetime.now()
#     return print(current_date - first_january )


# left_until_January()

# from datetime import datetime

# def left_until_January():
#     current_date = datetime.now() 
#     next_january = datetime(current_date.year + 1, 1, 1) #2025 +1
#     print(next_january)
#     time_left = next_january - current_date
    
#     days = time_left.days
#     print(days) # 322
#     hours, remainder = divmod(time_left.seconds, 3600) # gives the total number of remaining seconds
#     minutes, seconds = divmod(remainder, 60)
    
#     print(f"Time left until January 1st: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# left_until_January()



#========= Exercise 6 : Birthday and minutes ==========
from datetime import datetime

# def how_much_you_live():
#     current_date = datetime.now() 
#     print(current_date)
#     input_from_user = input("Enter your b-day (YYYY-MM-DD): ")
#     date_of_birthday = datetime.strptime(input_from_user,"%Y-%m-%d") #converts the string into a datetime object
#     print(date_of_birthday)
#     time_left = current_date - date_of_birthday 
    
    # days = time_left.days
    # print(days) # 322
    # hours, remainder = divmod(time_left.seconds, 3600) # gives the total number of remaining seconds
    # minutes, seconds = divmod(remainder, 60)
    
#     total_minutes = time_left.total_seconds() // 60  

#     print(f"You have lived approximately {int(total_minutes):,} minutes.")

# how_much_you_live()

#=================== Exercise 7 : Faker Module ===============

from faker import Faker

fake = Faker()



def info_fake():
    users = []
    users.append({"name": fake.name(), "age": fake.age(), "email": fake.email()})
    return print(users)

info_fake()



