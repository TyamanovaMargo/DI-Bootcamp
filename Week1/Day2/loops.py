# # # for <variable> in <iterable/sequene>
# #     #indented block of code

# # #looping on a sequennce (list)
# # fruits = ['apple',"bananan",'kiwi','pear']

# # for each_fruit in fruits:
# #     print(each_fruit)

# # #looping on a range of numbers

# # #range (start, stop, stop)
# # for i in range(5): # four times it stop before the 5
# #     print(i)
# # for i in range(1,5): # start and last point
# #     print(i)
# # for i in range(1,2,10): 
# #     print(i)


# # # enumerate()
# # fruits = ['apple',"bananan",'kiwi','pear']

# # for i,each_fruit in enumerate(fruits):
# #     if each_fruit == fruits[3]:
# #         print("this is last one")
# #     print(i,each_fruit)

# # for i, each_fruit in enumerate(fruits):
# #     if each_fruit == "kiwi":
# #         fruits[1] == "lime"
# #     else:
# #         print(each_fruit)
# # print(fruits)


# # # exercise 4

# # number_from_user = int(input("Give me a number"))

# # for i in range(1,11):
# #     print(number_from_user * i)

# #While loop

# i = 0
# while i < 5:
#     print(1)
#     i += 12

# fruits = ['apple',"bananan",'kiwi','pear']

# i = 0 #counter
# while i < len(fruits):
#     print(fruits[i])
#     i += i

# pizzas_order = []
# max_pizza = 5


# # while len(pizzas_order) < max_pizza:
# #     flavor = input('which flavor?( if you finished  type "done")')

# #     if flavor == "done":
# #         print("Succsesful added")
# #         break;
# #     pizzas_order.append(flavor)

# while True:
#     flavor = input('which flavor?( if you finished  type "done")')

#     if flavor == "done":
#         print("Succsesful added")
#         print(pizzas_order)
#         break;
#     pizzas_order.append(flavor)
