###################################################################################
# The user is prompted for a name and is greeted (User 1 and User 2)
# The user is asked to select with X or O
# The user is displayed the rules
# The User gets to play both turns. Everytime the user plays, the X and O switch
# If there is a winner, the winner is declared
# In case of Stalemate, Stalemate is declated
# Ask user if they want to play again
###################################################################################


# Funciton for Validating Position
def valPos(pos):
    valid = True

    x = int((pos - 1) / 3)
    y = (pos - 1) % 3

    if tictactoe[x][y].strip() != "":
        valid = False

    return valid

# Setting the value at the position
def setVal(pos, turn):
    x = int((pos - 1) / 3)
    y = (pos - 1) % 3

    if turn:
        tictactoe[x][y] = xosel['user1']
    else:
        tictactoe[x][y] = xosel['user2']

    showTicTacToe()


# Printing the Tic Tac Toe on the page
def showTicTacToe():
    print(f"\t\t{tictactoe[0][0]}|{tictactoe[0][1]}|{tictactoe[0][2]}\n\t\t-+-+-\n\t\t{tictactoe[1][0]}|{tictactoe[1][1]}|{tictactoe[1][2]}\n\t\t-+-+-\n\t\t{tictactoe[2][0]}|{tictactoe[2][1]}|{tictactoe[2][2]}")

# Find Winner

def checkWinner():

    if tictactoe[0][0] == tictactoe[0][1] == tictactoe[0][2] != " " or tictactoe[1][0] == tictactoe[1][1] == tictactoe[1][2] != " " or tictactoe[2][0] == tictactoe[2][1] == tictactoe[2][2] != " " or tictactoe[0][0] == tictactoe[1][0] == tictactoe[2][0] != " " or tictactoe[0][1] == tictactoe[1][1] == tictactoe[2][1] != " " or tictactoe[0][2] == tictactoe[1][2] == tictactoe[2][2] != " " or tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] != " " or tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] != " ":
        return True

    return False

#==========================================================================
# Declare the Tic Tac Toe
tictactoe = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
xosel = {'user1':'X','user2':'O'}
whoseturn = True
play = 9
gameon = True

while gameon:
    # Ask User for Inputs - Name and Selection
    user1 = input("\t > Please provide your name (User 1) encode: ").strip().capitalize()
    user2 = input("\t > Please provide your name (User 2) encode: ").strip().capitalize()
    xoro = input("\t > Select either 'X' or 'O' for the game (for User 1) : ").strip().capitalize()

    if xoro != 'X':
        xosel['user1'] = 'O'
        xosel['user2'] = 'X'
        

    print(f"\t\t @@ Welcome {user1}, you have chosen '{xosel['user1']}' @@")
    print("\t\t @@ Welcome {}, you have chosen '{}' @@".format(user2,xosel['user2']))

    # Display Rules to the User
    with open("./tictactoe_rules.txt") as rules:
        content = rules.readlines()

    for line in content:
        print (line)


    while play != 0:
        # Ask User to Select Position
        position = input(" > Select a position (Numbers between 1 - 9): ").strip()
        pos = int(position)

        # Check Position is valid
        if not valPos(pos):
            continue

        # If true, set X or O at position and display
        setVal(pos, whoseturn)    

        # Check Winner
        if checkWinner():
            print ("You are the Winner in this Game!!")
            play = 0
            break

        # Check Stalemate
        play = play - 1

        if play == 0:
            print("\t > The Game is a Stalemate!! Better luck next time!!")
            
        whoseturn = not whoseturn
        

    # Ask user for another game
    game = input(" > Do you want to play again? (Y or N) : ").strip().capitalize()
    if game != 'Y':
        gameon = False








