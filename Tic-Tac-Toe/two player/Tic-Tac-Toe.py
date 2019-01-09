###################################################################################
# The user is prompted for a name and is greeted (User 1 and User 2)
# The user is asked to select with X or O
# The user is displayed the rules
# The User gets to play both turns. Everytime the user plays, the X and O switch
# If there is a winner, the winner is declared
# In case of Stalemate, Stalemate is declated
# Ask user if they want to play again
###################################################################################

# Reset the Tic Tac Toe
def resetGame():
    return [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],9]
    


# Finding tic-tac-toe position from user input position
def findTicTacToePosFromUserPos (pos):

    x = int((pos-1)/3)
    y = (pos-1) %3

    return [x,y]

# Funciton for Validating Position
def valPos(pos):
    valid = True

    TicTacToePos = findTicTacToePosFromUserPos(pos)

    if tictactoe[TicTacToePos[0]][TicTacToePos[1]].strip() != "":
        valid = False

    return valid

# Setting the value at the position
def setVal(pos, turn):
    TicTacToePos = findTicTacToePosFromUserPos(pos)

    if turn:
        tictactoe[TicTacToePos[0]][TicTacToePos[1]] = xosel['user1']
    else:
        tictactoe[TicTacToePos[0]][TicTacToePos[1]] = xosel['user2']

    showTicTacToe()


# Printing the Tic Tac Toe on the page
def showTicTacToe():
    printTicTacToe = "\t\t"
    for pos in range(1,10):
        TicTacToePos = findTicTacToePosFromUserPos(pos)
        printTicTacToe = printTicTacToe + tictactoe[TicTacToePos[0]][TicTacToePos[1]]
        if pos != 9:
            if pos % 3 == 0 :
                printTicTacToe = printTicTacToe + "\n\t\t-+-+-\n\t\t"
            else:
                printTicTacToe = printTicTacToe + "|"

    print (printTicTacToe)
    

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

    # Resetting the params at the start of the new Game
    gameparams = resetGame()
    tictactoe = gameparams[0]
    play = gameparams[1]
    whoseturn = True
    
    # Ask User for Inputs - Name and Selection
    user1 = input("\t > Please provide your name (User 1) encode: ").strip().capitalize()
    user2 = input("\t > Please provide your name (User 2) encode: ").strip().capitalize()
    xoro = input("\t > Select either 'X' or 'O' for the game (for User 1) : ").strip().capitalize()

    if xoro != 'X':
        xosel['user1'] = 'O'
        xosel['user2'] = 'X'
        whoseTurn = False
    else:
        xosel['user1'] = 'X'
        xosel['user2'] = 'O'
        

    print(f"\t\t @@ Welcome {user1}, you have chosen '{xosel['user1']}' @@")
    print("\t\t @@ Welcome {}, you have chosen '{}' @@".format(user2,xosel['user2']))

    # Display Rules to the User
    with open("./tictactoe_rules.txt") as rules:
        content = rules.readlines()

    for line in content:
        print (line)

    print(play)
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
    print (game)
    if game != 'Y':
        gameon = False









