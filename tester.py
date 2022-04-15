from tictactoe import check_diagonal, check_horizontal, check_vertical, initial_state, actions, winner, terminal, utility, minimax, player, max_value, min_value

import pprint

X = "X"
O = "O"
EMPTY = None

def test_state():
    """
    Returns starting state of the board.
    """
    return [[X, X, O],
            [O, O, X],
            [X, EMPTY, EMPTY]]

def test_state2():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, O, X],
            [X, X, O],
            [EMPTY, EMPTY, EMPTY]]

if __name__ == "__main__":
    board = initial_state()
    # board = test_state()
    # board = test_state2()

    # for i in range(3):
    #     for j in range(3):
    #         board[i][j] = O

    # board[0][2] = X
    # board[1][1] = X
    # board[2][0] = X
    
    # board[0][0] = O
    # board[1][1] = O 
    # board[2][2] = O

    # board[0][0] = X
    # board[1][0] = X
    # board[2][0] = X
    
    # board[0][1] = O
    # board[1][1] = O
    # board[2][1] = O

    # board[0][0] = X
    # board[0][1] = X
    # board[0][2] = X

    # board[2][0] = X
    # board[2][1] = X
    # board[2][2] = X
    
    pprint.pprint(board, width=40)

    # print(player(board))

    # print(check_horizontal(board))
    # print(check_vertical(board))
    # print(check_diagonal(board))

    # print(winner(board))
    # print(terminal(board))
    # print(utility(board))
    
    # print(actions(board))

    # print(min_value(board))
    # print(max_value(board))
    print(minimax(board))

    # print(min_value(board))
