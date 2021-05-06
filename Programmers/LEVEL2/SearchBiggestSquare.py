# 14. 가장 큰 정사각형 찾기
import numpy as np

# 동적 계획법으로 푸는 문제
def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1],
                                  board[i - 1][j - 1]) + 1

    answer = max([num for row in board for num in row]) ** 2
    return answer

board_1 = [[0, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 1, 0]]
board_2 = [[0, 0, 1, 1],
           [1, 1, 1, 1]]

print(solution(board_1))
print(solution(board_2))

def solution_mine(board):
    answer = 0

    board_arr = np.array(board)
    # 행, 열 1의 개수 담는 리스트
    row_lst, col_lst = [], []
    # 정사각형 길이 리스트
    square_lst = []

    for row in board:
        row_cnt = row.count(1)
        col_lst.append(row_cnt)

    for col in range(len(board[0])):
        column_lst = list(board_arr[:, col])
        col_cnt = column_lst.count(1)
        row_lst.append(col_cnt)

    print(col_lst, row_lst)
    return answer