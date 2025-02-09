
import random


answer_from_user = input("Give me a string:")
letter_new = ''
#==================== Bonus =======================
# 1- convert the string to a list
answer_from_user_shuffled = list(answer_from_user)
# 2 - shuffle it
random.shuffle(answer_from_user_shuffled)
# 3 -  join the result again
result_of_shuffles_answer = ''.join(answer_from_user_shuffled)
#==================== Bonus ========================


print(f'A new string: {result_of_shuffles_answer}')

if len(result_of_shuffles_answer) < 10 :
        print('string not long enough')
elif len(result_of_shuffles_answer) > 10 :
        print('string too long')
else: 
      print('Perfect string')
      print(f' First letter: {result_of_shuffles_answer[0]} and Last letter: {result_of_shuffles_answer[9:]}') # first and last letter
      for letter in   answer_from_user_shuffled : #construct the string character by character
        letter_new = letter_new + letter[0]
        print(letter_new)