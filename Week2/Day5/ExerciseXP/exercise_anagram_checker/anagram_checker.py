#Create a new file called anagram_checker.py which contains a class called AnagramChecker.


import itertools  # itertools.permutations is used to generate all possible anagrams of a given word.


class AnagramChecker:
    def __init__(self,filename):
        self.filename = filename
        with open(filename, "r", encoding="utf-8") as file:
            # self.word_set = set(file.read().splitlines()) # without dublicate
            self.word_set = {line.strip() for line in file} 


    def is_valid_word(self,word):
        return word.upper() in  self.word_set


    def get_anagrams(self,word):
        # letters = list(word.upper())
        # print(letters) # ['m', 'e', 'a', 't']
        word = word.upper()
        # perms = itertools.permutations(word) # The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations,
        # print(perms) # <itertools.permutations object at 0x104737830>
        perms = {''.join(p) for p in itertools.permutations(word)} #  permutations 
        # print(word_lst)
        # anagram_lst = set(w for w in word_lst if w in self.word_set and w != word)
        anagram_lst = sorted(perms & self.word_set - {word}) #without original word
        return anagram_lst
        




# test = AnagramChecker('sowpods.txt')
# test.is_valid_word('MEAT')
# print(test.get_anagrams('MEAT'))

# import os
# print(os.listdir())  # Покажет список файлов в папке
