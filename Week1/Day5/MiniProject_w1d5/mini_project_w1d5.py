
board = [
    [' ', ' ', ' '], #[0]   
    [' ', ' ', ' '],    
    [' ', ' ', ' '],     
    ]
'''
  [0][0] | [0][1] | [0][2]  
  -----------------  
  [1][0] | [1][1] | [1][2] 
  -----------------  
  [2][0] | [2][1] | [2][2]
'''
'''
0 (row=1 → 1-1=0)
1 (row=2 → 2-1=1)
2 (row=3 → 3-1=2)
'''
def display_board():
    
    print("*******************")  
    for i in range(3):
        print(f"* {board[i][0]}   | {board[i][1]}   | {board[i][2]}   *")
        if i < 2:
            print("* --- | --- |---  *")  # Separator between rows
    print("*******************")   #  border 


#take player input
def player_input(player):
    print(f"Player {player}'s turn...")
    
    while True :
        row = int(input("Enter row:")) # place in row
        col = int(input("Enter column:")) #place in column

        if row < 1 or row >3 or col < 1or col > 3:
            print("Wrong input")
        elif board[row-1][col-1] != ' ':
            print("This position is occupied")
        else:
            board[row -1][col -1] = player
            break


def check_win(player):
    # Check rows and columns
        for i in range(3):
        # rows
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            # columns
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        #diag
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
    
def main ():
    now_player = "X"  
    count = 0  

    while True:
        display_board() # To display the Tic Tac Toe board (GUI)
        player_input(now_player) # To get the position from the player. 
        count += 1

        if check_win(now_player): #To check whether there is a winner or not.
            display_board()
            print(f"Winner is {now_player}!")
            return

        if count == 9:  # If all cells are filled(3 * 3), it's a tie
            display_board()
            print("It's a tie!")
            return

        # Switch player
        if now_player == "X":
            now_player = "O"
        else:
            now_player = "X"


main()

