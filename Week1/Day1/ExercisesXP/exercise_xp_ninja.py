x = (1 == True) # = 1
y = (1 == False) # = 0
a = True + 4 # 1 + 4
b = False + 10 # 0 +10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum'''
print(len(my_text))




        
    
max_long_sentence = 0

while True: # try to asking
    sentence_from_user = input('Enter the longest sentence without the character "A": ')
    
    if "a" in sentence_from_user.lower(): # we transfomed all characters in lowcase and  check a include or not
        print("Your sentence contains the letter 'A'. Try again.")
        continue
    
    if len(sentence_from_user) > max_long_sentence:
        max_long_sentence = len(sentence_from_user)
        print(f"Congrats! New record: {max_long_sentence}")
