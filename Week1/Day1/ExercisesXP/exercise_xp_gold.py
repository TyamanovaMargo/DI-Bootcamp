#======== Exercise 1 ============
print("Hello world\n" * 4,"I love python\n" * 4)

#======== Exercise 2 ============
month_from_user = int(input("What month is it (1 to 12)?"))

if 3 <= month_from_user <= 5:
    print ("Spring")
elif 6 <= month_from_user <= 8 :
    print ("Summer")
elif 9 <= month_from_user <= 11 : 
    print ("Autumn")
else:
    print ("Winter")
