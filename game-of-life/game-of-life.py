import random
import time

DEAD = 0
LIVE = 1

def generate_dead_board(w,h):
    return [[DEAD for _ in range(h)] for _ in range(w)]


def generate_rand_board(w, h):
    board = generate_dead_board(w,h)
    for x in range(w):
        for y in range(h):
            rand_num = random.random()
            if rand_num >= .8:
                board[x][y] = LIVE
    return board

def next_board_state(board, w, h):
    next_board = generate_dead_board(w, h)
    for x in range(w):
        for y in range(h):
            next_state = next_cell_state(board, x, y)
            next_board[x][y] = next_state
    return next_board


def next_cell_state(board, x, y): 
    live_neighbors = get_live_neighbors(board, x, y)
    if (board[x][y] == LIVE):
        if (live_neighbors < 2): return DEAD
        elif (live_neighbors <= 3): return LIVE
        else: return DEAD
    else:
        if (live_neighbors == 3): return LIVE
        else: return DEAD
    

def get_live_neighbors(board, x, y):
    live_neighbors = 0
    width = len(board)
    height = len(board[0])
    for x1 in range((x-1), (x+1)+1): # (x+1)+1 so range sequence is from x-1 to x+1
        if (x1 >= 0 and x1 < width):
            for y1 in range((y-1), (y+1)+1):
                if (y1 >=0 and y1 < height):
                    if (y1 != y or x1 != x):
                        if (board[x1][y1] == LIVE):
                            live_neighbors+=1
    return live_neighbors

def pretty_print(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == LIVE:
                print(u'\u2b1c', end='')
            else:
                print(u'\u2b1b', end='')
        print()
        
def run_forever(board):
    next_state = board
    while True:
        pretty_print(next_state)
        next_state = next_board_state(next_state, len(next_state), len(next_state[0]))
        time.sleep(.03)

if __name__ == "__main__":
    board = generate_rand_board(50,50)
    run_forever(board)


