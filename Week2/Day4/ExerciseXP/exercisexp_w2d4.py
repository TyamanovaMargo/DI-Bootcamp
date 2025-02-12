#================== 🌟 Exercise 1 – Random Sentence Generator =======================
'''
Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

set → If you need unique words only (no duplicates).
list → If you need all words including duplicates (preserves order).
'''
import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,"sowpods.txt")




def get_words_from_file(file_path):
    with open(file_path) as f:
        words = f.read().split()
        return words
 #********************************************************************       
    #     words = set()  # Using a set to store unique words
    #     for line in f:
    #         words.update(line.strip().split())  # Splitting into words and adding to set
    # return print(words)

def get_random_sentence(word_list,length):
    
    random_words = random.sample(word_list,length)
    return " ".join(random_words).lower() + "."

def main():
        print("This program generates a random sentence from words in a file. (Between 2 and 20) ")

        len_from_user = int(input("Enter the number of words for the sentence (between 2 and 20): "))
        if len_from_user >=2 or len_from_user <= 20:
            return len_from_user
            
        else:
            print("Error")
            


        words_list = get_words_from_file(file_path)  # return list of words

        sentence = get_random_sentence(words_list, len_from_user) 
        # print(sentence)    

main()