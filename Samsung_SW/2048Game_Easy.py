# 삼성 SW 역량 기출문제 2. 2048(Easy)
from collections import deque

board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]
# print(board)

answer, que = 0, deque()

def get(row, column):
    # print('get function')
    # print(board[row][column])
    if board[row][column]:
        que.append(board[row][column])
        board[row][column] = 0
    # print('que :', que)

def merge(row, col, d_row, d_col):
    while que:
        # FIFO
        x = que.popleft()
        if not board[row][col]:
            board[row][col] = x
        elif board[row][col] == x:
            board[row][col] = x * 2
            row, col = row + d_row, col + d_col
        else:
            row, col = row + d_row, col + d_col
            board[row][col] = x

def move(one_dir):
    # Go up
    if one_dir == 0:
        for col in range(board_size):
            for row in range(board_size):
                get(row, col)
            merge(0, col, 1, 0)
    # Go down
    elif one_dir == 1:
        for col in range(board_size):
            for row in range(board_size - 1, -1, -1):
                get(row, col)
            merge(board_size - 1, col, -1, 0)
    # Go Right
    elif one_dir == 2:
        for row in range(board_size):
            for col in range(board_size):
                get(row, col)
            merge(row, 0, 0, 1)
    else:
        for row in range(board_size):
            for col in range(board_size - 1, -1, -1):
                get(row, col)
            merge(row, board_size - 1, 0, -1)

def solve_main(count):
    global board, answer

    if count == 5:
        for b_size in range(board_size):
            answer = max(answer, max(board[b_size]))

        return

    bef_board = [x[:] for x in board]

    # Move for Four Directions
    for four_dirs in range(4):
        move(four_dirs)
        solve_main(count + 1)
        board = [b_x[:] for b_x in bef_board]

    # print(board)

solve_main(0)
print(answer)