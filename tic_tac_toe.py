
from random import randrange
board = "-"*20
print(board)

mark=input("Do you want to play as x or o? ")
if mark=="x":
    print ("You chose x")
elif mark=="o":
    print ("You chose o")
else:
    mark=input("Invalid, choose x or o? ")

pc_mark=''
if mark=="x":
    print("computer is o")
    pc_mark="o"
else:
    print("computer is x")
    pc_mark="x" 


def evaluate(board):
    if "xxx" in board:
        print("X WINS")
        return "X"
    elif "ooo" in board:
        print("O WINS")
        return "O"
    elif "-" not in board:
        print ("It's a tie")
        return "!"
    else:
        return "-"
    

def player_move (board):
    place = int(input("Where do you want to place it? (0-19)? "))
    if board[place]=="-":
        board = board[:place] + mark + board[place + 1:]
    else:
        place = int(input("place occupied, try again "))
        board = board[:place] + mark + board[place + 1:]
 
    return board

def pc_move (board):
    """pc move"""
    place = randrange (0, 20)
    while board[place]!="-":
        place = randrange (0, 20)
        
    board = board[:place] + pc_mark + board[place + 1:]
    
    return board
    

def tictactoe (board):
    
    while evaluate(board)=="-":
        board=player_move (board)
        print(board)
        player_ev=evaluate(board)
        if player_ev!="-":
            break
        else:
            board=pc_move(board)
            print(board)
            pc_ev=evaluate(board)
            if pc_ev!="-":
                break
    return ''
    
print (tictactoe(board))

#To make the PC move smarter and make the game harder I think it should be:
#(for the explanation I'll sey player is x and PC is o)
#If xx or x-x in board put o next to x or between two x's to block the win
#elif put o next to an existing oo or o
#In other words the PC should first block a win and then try to make ooo, 
# if both goals possible in one move even better.


