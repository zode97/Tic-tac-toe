import random
import numpy as np
import matplotlib.pyplot as plt
import time
random.seed(1)
def create_board():
    board = np.zeros((3,3))
    return board
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
def possibilities(board):
    x = list(np.where(board == 0))
    return x 
def random_place(board, player):
    selections = possibilities(board)
    if len(possibilities(board)) >  0 :
        selection = random.choice(selections)
        place(board, player, selection)
        return board 
def row_win(board, player):
    for i in range(3):
        if board.all == player:
            return True 
        else:
            return False 
board = create_board()
def col_win(board, player):
    for i in range(3):
        if board[:i].all == player:
            return True 
        else:
            return False 
def diag_win(board, player):
    x =np.diag(board)
    if x.any == player:
        return True 
    else:
        return False  
def evaluate(board):
    winner = 0
    for player in [1, 2]:
       if row_win == True or col_win == True or diag_win == True:
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner 
def play_game():
    board = create_board()
    winer = evaluate(board)
    while winer== 1 or winer == 2:
        turn = random_place(board, 1)
        turn = random_place(board, 2)
    return winer
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            # use `random_place` to play a game, and store as `board`.
            winner = evaluate(board)
            # use `evaluate(board)`, and store as `winner`.
            if winner != 0:
                break
    return winner


start = time.clock()
for i in range(1000):
    play_strategic_game()
stop = time.clock()
x = time.time()
x = stop - start
print x 
plt.hist(x)
plt.show()   
