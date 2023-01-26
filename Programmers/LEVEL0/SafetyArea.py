# Restart 24. 안전지대

'''
My Solution : didn`t solve this problem by myself, but I change something
'''
def solution(board):
    answer = 0

    # 8 directions
    move_coords = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    booms = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                booms.append((row, col))

    # Re-initialize booms nearby areas to booms areas
    for boom_row, boom_col in booms:
        for dx, dy in move_coords:
            mx, my = boom_row + dx, boom_col + dy
            if 0 <= mx < len(board) and 0 <= my < len(board):
                board[mx][my] = 1

    # Count non-boom areas
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                answer += 1
    return answer

board_1 = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]]
board_2 = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0]]
board_3 = [[1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]]

print(solution(board_1))
print(solution(board_2))
print(solution(board_3))

'''
Using set for excepting boom areas
'''
def solution_other(board):
    answer = 0

    danger = set()
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if not col:
                continue
            danger.update((row_idx + di, col_idx + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])

    answer = len(board) * len(board) - sum(0 <= i < len(board) and 0 <= j < len(board) for i, j in danger)
    return answer

print(solution_other(board_1))
print(solution_other(board_2))
print(solution_other(board_3))

'''
Use numpy ndarray and apply ndarray`s padding
'''
import numpy as np
from collections import Counter
def solution_best(board):
    answer = 0

    board_padded = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    danger_array = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board_padded[row][col] == 1:
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        danger_array[x][y] = 1

    danger_list = danger_array.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    return answer

# print(solution_best(board_1))
# print(solution_best(board_2))
# print(solution_best(board_3))

'''
Use numpy ndarray different and it`s good.
'''
def solution_best_1(board):
    answer = 0

    board = np.array(board)
    for row, col in zip(*np.where(board == 1)):
        board[row - 1 if row else 0:row + 2, col - 1 if col else 0:col + 2] = 1

    answer = len(board[board == 0])
    return answer

# print(solution_best_1(board_1))
# print(solution_best_1(board_2))
# print(solution_best_1(board_3))