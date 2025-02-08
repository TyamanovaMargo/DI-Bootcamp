#========= Challenge 1 : Sorting ==========
'''

    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
    Use List Comprehension
'''

# word_from_user = input("Enter a comma-separated sequence of words: ") # also can split here


# result = [ word for word in word_from_user.split(",")] # Split the input 'items' into a list of words

# print(",".join(sorted(list(result))))


# =========== Challenge 2 : Longest Word ==========

'''
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
'''

sent = input("Enter a sentence: ")
def longest_word (sentence):
    longest_word = ''
    for word in sentence:
        if len(word) > len(longest_word):
            longest_word = word
    print (longest_word)




longest_word (sent.split(' ')) #Split into individual words