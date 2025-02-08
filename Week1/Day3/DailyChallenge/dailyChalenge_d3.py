#============ Challenge 1 =============
# word_from_user = input("Give me word: ")
# dict_of_word = {}
# dict(dict_of_word)

# # '''
# # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# #     Make sure the letters are the keys.
# #     Make sure the letters are strings.
# #     Make sure the indexes are stored in a list and those lists are values
# # '''
# for i,char in enumerate(word_from_user): # i - index, char -element
#     # print(f'{i},{char}')
#     if char in dict_of_word:
#         dict_of_word[char].append(i)
#     else: 
#         dict_of_word[char] = [i]
# print(dict_of_word)
    

#============ Challenge 2 =============
'''

    Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
    Sort the list in alphabetical order.
    Return “Nothing” if you can’t afford anything from the store.

Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)
'''
#===============================================

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

#===============================================


# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1"
#==================================

afford_in_the_store = []

for item , price in items_purchase.items():
    # print(item , price)
    cleaned_price = int(price.strip("$").replace(",","")) #strip delete just in the beginning
    cleaned_wallet = int(wallet.replace("$",""))
    # print(cleaned_wallet)
    if cleaned_price <= cleaned_wallet:
        afford_in_the_store.append(item)
        print(sorted(afford_in_the_store))
    else :
        print("Nothing")


