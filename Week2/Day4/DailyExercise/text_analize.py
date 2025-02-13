#=================== Text Analysis ==================

class Text:
    import os
    def __init__(self,text):
        self.text = text 

    def frequency_of_word (self, word):
        words = self.text.split(" ")    # ['A', 'good', 'book', 'would', 'sometimes', 'cost', 'as', 'much', 'as', 'a', 'good', 'house']
        # print(words)
        count = words.count(word)
        # print(count)
        if count ==0 :
            print("This word does not repeat")
        else :
            print(f"This {word} repet {count} times")
            return count 
    
    def most_common_word(self,word): # a method that returns the most common word in the text.
        count_dict = {}
        words = self.text.split(" ")

        for word in words:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1

        # return  print(max(count_dict.values()))
        # print(count_dict.items())
        max_count = max(count_dict.values())

        max_count_list = []

        for key,val in count_dict.items():
            if val == max_count:  
                return print(key, val)  

    def list_of_unique_words(self,word): # a method that returns a list of all the unique words in the text
        words = set(self.text.split(" "))
        return words

    @classmethod #transforms a regular method into a class method
    def from_file(cls, file_path: str):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return cls(text)




'''
Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

    Implement a classmethod that returns a Text instance but with a text file:

        >>> Text.from_file('the_stranger.txt')

    Hint: You need to open and read the text from the text file.

    Now, use the provided the_stranger.txt file and try using the class you created above.
'''
'''
Bonus:

    Create a class called TextModification that inherits from Text.

    Implement the following methods:
        a method that returns the text without any punctuation.
        a method that returns the text without any english stop-words (check out what this is !!).
        a method that returns the text without any special characters.

Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.'''



# text_text = Text("A good book would sometimes cost as much as a good house")
# text_text.frequency_of_word('look')
# text_text.most_common_word(text_text)
# print(text_text.list_of_unique_words(text_text))
# print(text_ob.text)

text = "A good book would sometimes cost as much as a good house."
text_instance = Text(text)

import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,'the_stranger.txt')

text_in_file = Text.from_file(file_path )
print( text_in_file.most_common_word())         
print( text_in_file.unique_words())               


                                
