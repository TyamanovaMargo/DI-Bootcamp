words = [] #creat list
words.append(input("Enter 7 words: "))
letter = input(("Enter a single character: "))

for i,char in enumerate(words[0]):
    if char == letter:
        print(f'the index {i} of the first appearence of the letter variable in each word of the list')
        break
    else :
        print("letter doesn’t exist")
        break