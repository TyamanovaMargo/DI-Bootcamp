# ======= Exercise 1: Concatenate lists ======
# Write code that concatenates two lists together without using the + sign.

list1 = [23,45,6,75]
list2 = [56, 784, 89]
list1.extend(list2)
print(list1)

#==========Exercise 2: Range of numbers ======
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for i in range(1500,2500):
    if i % 5 == 0 and i % 7 == 0:
        print(i)