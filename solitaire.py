import sys
print("\n")
print("HELLO! WELCOME TO MARBLE SOLITAIRE GAME")
print("\n")
print("about game:")
print("*This is one player game")
print("*The game consists of 32 marbles")
print("*Initially an empty hole is in the middle")
print("*Remaining positions are filled with marbles")
print("*The board has 7 rows and 7 columns refered with indexes 0 to 6")  
print("*Empty positions are indicated by '0'")
print("*Marble filled positions are indicated by '1'")
print("*If you end up with only one marble left you will WIN otherwise you will loose the game")
print("\n")
print("How to play?")
print("Simply jump one marble over another marble")
print("While jump from one position to another position make sure that the position have marble and the position you want to jump is empty")
print("\n")
name = input("enter player name:")
print("\n")
print("     ***** RULES *****    ")
print("\n")
print("-> u or U is used for upward move")
print("-> d or D is used for downward move")
print("-> l or L is used for leftside move")
print("-> r) or R is used for rightside movie")
print("\n")
board = [[" "," ","1","1","1"," "," "],[" "," ","1","1","1"," "," "],["1","1","1","1","1","1","1"],["1","1","1","0","1","1","1"],["1","1","1","1","1","1","1"],[" "," ","1","1","1"," "," "],[" "," ","1","1","1"," "," "]]

#The function display_board is used to display the status of game

def display_board():
    for i in range(7):
        for j in range(7):
            print(board[i][j], end=" ")
        print("\n")
display_board()
def game():
    mode = input("Choose l for left..choose r for right..choose u for up..choose d for down:").lower()

    #If case is evaluated when left mode is given

    if mode == "l":
        print("You choose left")
        print("Please enter position to move by giving row and column num in range 0 to 6:")
        i = int(input("Row number:"))
        j = int(input("Column number:"))
        pos = board[i][j]
        if pos != " " and pos != "0" and board[i][j-1] == "1" and board[i][j-2] == "0":
            board[i][j] = "0"
            board[i][j-1] = "0"
            board[i][j-2] = "1"
            display_board()
            print("move successful")
            return 1
        else:
            print("Sorry! Invalid move")
            display_board()
            return -1
    #If case is evaluated when right mode is given

    if mode == "r":
        print("You choose right")
        print("Please enter position to move by giving row and coloumn num in range 0 to 6:")
        i = int(input("Row number:"))
        j = int(input("Column number:"))
        pos = board[i][j]
        if pos != " " and pos != "0" and board[i][j+1] == "1" and board[i][j+2] == "0":
            board[i][j] = "0"
            board[i][j+1] = "0"
            board[i][j+2] = "1"
            display_board()
            print("move successful")
            return 1
        else:
            print("Sorry! Invalid move")
            display_board()
            return -1
    
    #If case is evaluated when up mode is given

    if mode == "u":
        print("You choose up")
        print("Please enter position to move by giving row and coloumn num in range 0 to 6:")
        i = int(input("Row number:"))
        j = int(input("Column number:"))
        pos = board[i][j]
        if pos != " " and pos != "0" and board[i-1][j] == "1" and board[i-2][j] == "0":
            board[i][j] = "0"
            board[i-1][j] = "0"
            board[i-2][j] = "1"
            display_board()
            print("move sucessful")
            return 1
        else:
            print("Sorry! Invalid movie")
            display_board()
            return -1
    
    #If case is evaluated when down mode is given

    if mode == "d":
        print("You choose down")
        print("Please enter position to move by giving row and coloumn num in range 0 to 6:")
        i = int(input("Row number:"))
        j = int(input("Column number:"))
        pos = board[i][j]
        if pos != " " and pos != "0" and board[i+1][j] == "1" and board[i+2][j] == "0":
            board[i][j] = "0"
            board[i+1][j] = "0"
            board[i+2][j] = "1"
            display_board()
            print("move successful")
            return 1
        else:
            print("Sorry! Invalid move")
            display_board()
            return -1
c = 0        
for k in range(36):
    r = game()
    if r == 1:
        c += 1
    if c == 31:
        sys.exit("Congratulations!!..You won the game")
print("Oops!..sorry no more moves..You lost the game")
