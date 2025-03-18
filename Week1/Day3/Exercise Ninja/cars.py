cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

cars = cars_string.split(",")
# print(type(cars))
# print(cars)


print(f'manufacturers/companies are {len(cars)}')
print(f'manufacturers/companies are {sorted(cars)}')


# [выражение for элемент in последовательность if условие]

count_o = 0
count_no_i = 0

for car in cars:
    if "o" in car.lower():
        count_o += 1
    if "i" not in car.lower():
        count_no_i += 1

print("with letter  'o':", count_o)     
print("without letter 'i':", count_no_i)  


# bonus

cars = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_cars = list(set(cars))
unique_cars_string = ','.join(unique_cars)
print(unique_cars_string)

#Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
# sorted
sorted_cars = sorted(cars)

# revers letters
reversed_sorted_cars = [car[::-1] for car in sorted_cars]

print(reversed_sorted_cars)