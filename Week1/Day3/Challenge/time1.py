#1

# reverse_inp = input("Enter a string: ")



# reversed = reverse_inp[::-1]



# print(reversed) 



#2

number = int(input("Give me a number: "))


Sum = 0
for i in range(1, number):
    if(number % i == 0):
        Sum = Sum + i
if (Sum == number):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")
