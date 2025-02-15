

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))# 0,1,2

# computer_choice = random.randint( 0, 2)
# print(f"Computer chose {computer_choice}")

# if user_choice == 0 and computer_choice == 2:
#     print("Ypu win")
# elif computer_choice == 0 and user_choice == 2
#     print("Ypu losee")
# elif computer_choice > user_choice:
#      print("Ypu losee")
# elif computer_choice == user_choice:
#      print("it's a draw")
# else :
#      print("You typed an ivalid number")


import random


class Game : 
    def __init__(self):
        
        self.game_images =["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
            _______
        ---'    ____)_
                ______)
                _______)
                _______)
        ---.__________)
        """,

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
        self.choices= ["rock", "paper", "scissors"]
        
        
    def get_user_item(self):
            # user_choice = input("Select (r)ock, (p)aper, (s)cissors:  ").lower()
            while True:
                user_choice = input("Select (r)ock, (p)aper, (s)cissors:  ").lower()
                if user_choice not in ["r","p","s"]:
                  print("Not valid. Try again")
                else:
                    if user_choice == "r":
                          return "rock",self.game_images[0]
                    elif user_choice == "p":
                         return "paper",self.game_images[1]
                    elif user_choice == "s":
                         return "scissors",self.game_images[2]
                         



    def get_computer_item(self):
            computer_choice = random.choice(self.choices)
            if  computer_choice == "rock":
                 return "rock",self.game_images[0]
            elif computer_choice == "paper":
                return "paper",self.game_images[1]
            elif computer_choice == "scissors":
                return "scissors",self.game_images[2]
    
    def get_game_result(self, user_choice, computer_choice):
        var = { #The dictionary keys are tuples containing two choices (user's choice and computer's choice).
            ("rock", "scissors"): "win",
            ("scissors", "paper"): "win",
            ("paper", "rock"): "win",
            ("scissors", "rock"): "loss",
            ("paper", "scissors"): "loss",
            ("rock", "paper"): "loss",
        }
        if user_choice == computer_choice:
            result = "draw"
        else:
            result = var.get((user_choice, computer_choice), "loss")  

        if result == "win":
            print("You win")
        elif result == "loss":
            print("You lose")
        else:
            print("It's a draw")

        return result
    def play(self):
        """Runs a single round of the game."""
        user_choice, user_image = self.get_user_item()
        computer_choice, computer_image = self.get_computer_item()

        print("\nYou chose:")
        print(user_image)
        print("\nComputer chose:")
        print(computer_image)

        return self.get_game_result(user_choice, computer_choice)

         
        
         

round = Game()
user_choice, user_image = round.get_user_item()
computer_choice, computer_image = round.get_computer_item()

# Вывод выбора пользователя и компьютера
print(f"\nYou chose: {user_choice}\n{user_image}")  
print(f"\nComputer chose: {computer_choice}\n{computer_image}")  

# Определяем и печатаем результат
round.get_game_result(user_choice, computer_choice)  # Здесь уже есть print внутри метода

