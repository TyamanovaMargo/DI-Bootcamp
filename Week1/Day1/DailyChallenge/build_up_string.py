answer_from_user = input("Give me a string:")
letter_num = ""
if len(answer_from_user) < 10 :
        print('string not long enough')
elif len(answer_from_user) > 10 :
        print('string too long')
else: 
      print('Perfect string')
      print(f' First letter: {answer_from_user[0]}')
      print(f' Last letter: {answer_from_user[9:]}')
      for letter in   answer_from_user :
        letter_num = letter_num + letter[0]
        print(letter_num)
        



