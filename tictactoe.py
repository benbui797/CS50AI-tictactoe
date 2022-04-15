"""
Tic Tac Toe Player
"""

import copy
import math
from random import randint

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    Count amount of X's and O's to determine who's turn it is.

    Return X in case of draw.
    """

    x = 0
    o = 0

    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1

    if o < x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    Loop through board and store EMPTY cells as tuple where i = row and j = column.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add(tuple([i, j]))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    If cell is not empty, else raise error
    Else return deepcopy of board with the action applied to it
    """

    i, j = action
    
    if board[i][j] is not EMPTY:
        raise RuntimeError
        
    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_horizontal(board) is not None:
        return check_horizontal(board)
    elif check_vertical(board) is not None:
        return check_vertical(board)
    elif check_diagonal(board) is not None:
        return check_diagonal(board)
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    Return True if there is a winner
    Else check if no EMPTY cells on board.
    """

    if winner(board) != None:
        return True
    
    counter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                counter += 1
    
    if counter == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    Player X wins if Utility returns 1, so X wants to maximise the result.
    O wants to minimize utility.

    If the AI starts as X, often it would place first move in a edge, which is not optimal...
    So I import random and let the AI pick either center or corner randomly
    """  
    
    # check if board is empty (first move)
    if board == initial_state():
        random = randint(1, 5)
        if random == 1:
            return (0, 0)
        elif random == 2:
            return (0, 2)
        elif random == 3:
            return (2, 0)
        elif random == 4:
            return (2, 2)
        elif random == 5:
            return (1, 1)
        print(random)

    move = None

    if terminal(board):
        return None
    
    # if player = X -> Optimum = 1 -> Maximise v
    if player(board) == X:
        v = -math.inf

        # loop through actions and store highest possible v value
        for action in actions(board):
            action_v = max_value(result(board, action))
            print(f"{action_v=} {action=}") 
            if action_v > v:
                v = action_v
                move = action
                print(f"{v=} {move=}")
            
    # else player = O -> optimum = -1 -> max_v as small as possible
    else:
        v = math.inf

        # loop through actions and store minimum possible v value
        for action in actions(board):            
            action_v = min_value(result(board, action))  
            print(f"{action_v=} {action=}")      
            if action_v < v:
                v = action_v
                move = action
                print(f"{v=} {move=}")
    
    # return best move                
    return move

 
def max_value(board):
    """
    Returns max v value for an action
    """

    # if board is full, return utility value(1, 0 or -1)
    if terminal(board):
        return utility(board)
    
    # initialise v to negative infinity so any move will have higher v value.
    # then check v value against min value (recursive) and store highest value in v.
    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v
    

def min_value(board):
    """
    Returns min v value for an action
    """
    
    # if board is full, return utility value(1, 0 or -1)
    if terminal(board):
        return utility(board)
    
    # initialise v to infinity so any move will have lower v value.
    # check v against max_value (recursively) and store lowest v value.
    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def check_horizontal(board):
    """
    Check horizontal axis for 3 in a row.
    """

    for i in range(3):
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O

    return None        


def check_vertical(board):
    """
    Check vertical axis for 3 in a row.
    """

    for i in range(3):
        if board[0][i] is not EMPTY:
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

    return None


def check_diagonal(board):
    """
    Check diagonal axis for 3 in a row.
    """
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    else:
        return None
    