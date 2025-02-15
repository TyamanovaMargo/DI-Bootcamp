from anagram_checker import AnagramChecker



def main():

        anagram_check = AnagramChecker('sowpods.txt')

        while  True:
            input_from_user = input('Enter a word or enter "exit"?').strip()
            if input_from_user == "exit":
                break
            if len(input_from_user.split()) > 1:
                print("Error : more the one word")
                continue
            elif not input_from_user.isalpha() :
                    print("Error : Only alphabetic characters are allowed. No numbers or special characters. ")
                    continue

            elif not anagram_check.is_valid_word(input_from_user):
                    print(f"Error: The word '{input_from_user}' is not in the dictionary.")


            else :
                    print(f"Your word: {input_from_user}")
                    print(f"Valid word ")
                    anagrams = anagram_check.get_anagrams(input_from_user)
                    print(f'Anagrams for your word: {", ".join(anagrams)}.')
            
            
        
            

main()