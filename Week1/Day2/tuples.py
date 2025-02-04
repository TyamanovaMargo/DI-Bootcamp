# Tuples: immutable( not can be changed)  and ordered 

numbers  = (10,20,30,40,20,50,20)
print(type(numbers))

#tuples method 
print(numbers.count(20))
print(numbers.index(30))

#concatenate tuples
number2 = (2,3,5,7)
mixed_tuples = numbers + number2
print(mixed_tuples)

 #unpacking a tuple
a,b,c,d = (5,10,15,20)
print(a)

#example that you can unpack variables not only typles
name, age, email = "juliana",27, 'mail.com'


# exercise 2
a_tuple = (10,20,30,40)
a,b,c,d = a_tuple
print(f'{a},{b},{c},{d}')

#Sets = unordered data structure

my_set = {1,4,8,9}
# my_set = set()

my_set.add(12)
my_set.add(55)
print(my_set)

# we cant accese index in set

id_numbers = [123,56,75634,235,5678,567,123]
unique_ids = set(id_numbers)
print(unique_ids)

names = {"julian","israel","dina"}
country_names = {"usa","brazil","israel"}

print(names.intersection(country_names))

names_and_countries = names.union(country_names)
print(names_and_countries)#it does union and delete duplicate

print(country_names.difference(names))

names.clear()
print(names)

# exercise 3 

my_favorite_numbers = {18,69,13,25,4}

my_favorite_numbers.add(88)
print(my_favorite_numbers)

set_of_prime_nimbers = {2,3,7,13,17}
print(my_favorite_numbers.intersection(set_of_prime_nimbers))

my_favorite_numbers.clear()
print(my_favorite_numbers)