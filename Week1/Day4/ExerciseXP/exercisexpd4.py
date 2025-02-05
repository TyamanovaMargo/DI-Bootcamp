# #=========== 🌟 Exercise 1 : What are you learning ?==========

# '''

#     Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#     Call the function, and make sure the message displays correctly.
# '''
# def display_message():
#      print("I'm learning how to analyze data effectively using tools like SQL, Python, and visualization techniques to derive meaningful insights")

# display_message()


# #==================== 🌟 Exercise 2: What’s your favorite book ? =================
# '''

#     Write a function called favorite_book() that accepts one parameter called title.
#     The function should print a message, such as "One of my favorite books is <title>".
#     For example: “One of my favorite books is Alice in Wonderland”
#     Call the function, make sure to include a book title as an argument when calling the function.
# '''

# def favorite_book(title : str):
#      print(f'One of my favorite books is {title}')

# favorite_book("Norwegian Wood")



# #====================🌟 Exercise 3 : Some Geography =================

# '''

#     Write a function called describe_city() that accepts the name of a city and its country as parameters.
#     The function should print a simple sentence, such as "<city> is in <country>".
#     For example “Reykjavik is in Iceland”
#     Give the country parameter a default value.
#     Call your function.
# '''

# def describe_city(name_of_city, country = "Japan"):
#      print(f'{name_of_city} is in {country}')

# describe_city("Seoul","Korea")

# #========= Exercise 4 : Random ==============
# '''
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# '''
import random

# def random_func (number):
#     number2 =random.randrange(1,100)
#     if number == number2:
#         print("The same numbers. Great!")
#         return True
#     else:
#          print("The different")
#          return False

# while True :
#     number = int(input("Enter a number: "))
#     if random_func(number): # if func return True to do break
#          break
    

#=============== 🌟 Exercise 5 : Let’s create some personalized shirts ! =================
'''

    Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
    Call the function make_shirt().

    Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
    Call the function, in order to make a large shirt with the default message
    Make medium shirt with the default message
    Make a shirt of any size with a different message.

    Bonus: Call the function make_shirt() using keyword arguments.
'''

# def make_shirt(size = "large",text = "I love Python"):
#      print(f'The size of the shirt is {size} and the text is {text}')



# make_shirt('large')
# make_shirt('medium')
# make_shirt("small","Hello")


# #==========Bonus =======================
# def make_shirt(**kwargs):
#         print(f'The size of the shirt is {kwargs["size"]} and the text is {kwargs["text"]}')

# make_shirt(size ="XXl",text ="Hi")

#===============  🌟 Exercise 6 : Magicians =============
'''
Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

    Create a function called show_magicians(), which prints the name of each magician in the list.
    Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
    Call the function make_great().
    Call the function show_magicians() to see that the list has actually been modified.
'''

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# # def show_magicians(**kwargs):
# #     for each in kwargs["magician_names"]:
# #         print(each)

# # show_magicians(magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'])

# def make_great(**kwargs):
#     magician_names_modif = []
#     for each in kwargs["magician_names"]:
#         new_each = "the Great"+each
#         magician_names_modif.append(new_each)
#     return print(magician_names_modif)


# make_great(magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'])   

#===============  🌟 Exercise 7 : Temperature Advice =============
'''
Create a function called get_random_temp().

    This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
    Test your function to make sure it generates expected results.
'''
# def get_random_temp():
#     number = random.randrange(-10 ,40 )
#     return number



'''
Create a function called main().

    Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
    Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
'''


'''
Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:

    below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
    between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
    between 16 and 23
    between 24 and 32
    between 32 and 40
'''


'''
Change the get_random_temp() function:

    Add a parameter to the function, named ‘season’.
    Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
'''
#Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
# def months_to_season(month):
#     if month == 12 or month == 1 or month == 2:
#         return "winter"
#     if month == 3 or month == 4 or month == 5:
#         return "spring"
#     if  month == 6 or month == 7 or month == 8:
#         return "summer"
#     else: 
#         "autumn"


# def get_random_temp(season):
#     if season == "winter":
#         number = random.uniform(-10,16) #Bonus: Give the temperature as a floating-point number instead of an integer. uniform
#     elif season == "spring":
#         number = random.uniform(16,23)
#     elif season == "autumn":
#         number = random.uniform(24,32)
#     else: 
#         number = random.uniform(32,40)
#     return number

# def main():
#     # temperature = get_random_temp()
#     # print(f'The temperature right now is {temperature} degrees Celsius.')
#     month = int(input("Enter a month number (1-12): "))
#     season =  months_to_season(month)  
#     temperature = get_random_temp(season) 
#     # print(f'The temperature right now is {temperature} degrees Celsius.') 

#     if temperature < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly!")
#     elif 16 < temperature <= 23:
#         print("Nice weather!")
#     elif 24 <= temperature <= 32:
#         print("Warm and pleasant!")
#     elif 32 < temperature <= 40:
#         print("It’s hot!")
#     else:
#         print("Temperature is above 40°C!")

#     print(f'The temperature right now is {temperature} degrees Celsius.') 


# main()

# get_random_temp("Autumn")
# seasons = ["Spring", "Summer", "Autumn", "Winter"]
# season_random = random.choice(seasons)
# get_random_temp(season_random)


'''
Now that we’ve changed get_random_temp(), let’s change the main() function:

    Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
    Use the season as an argument when calling get_random_temp().
'''

#========================== 🌟 Exercise 8 : Star Wars Quiz =======================
'''
This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers
'''
#=====🌟 Exercise 8 : Star Wars Quiz ===============

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
#Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers

def answers_from_user (data):
    count_answers = 0
    wrong_answers = []
    for element in data:
        print(element["question"])
        answer = input("Your answer: ")
        if element["answer"] == answer:
            count_answers += 1
            
        else:
            wrong_answers.append(answer)
    return count_answers, wrong_answers

def info_for_user(right_answers ,wrong_answers):
    print(f"The number of correct answers is {right_answers} and the list of incorrect answer is {len(wrong_answers)}")
    if wrong_answers:
        for question in wrong_answers:
            print(question)
     


def main():
    right_answers ,wrong_answers = answers_from_user(data) #we have to say result from func 
    info_for_user(right_answers ,wrong_answers)

main()