# 9. 크레인 인형뽑기 게임
import numpy as np

def solution(board, moves):
    answer = 0

    # 바구니 리스트
    bucket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0

                if bucket[-1:] == bucket[-2:-1]:
                    answer += 2
                    bucket = bucket[:-2]
                break

    return answer


board_1 = [[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 3],
           [0, 2, 5, 0, 1],
           [4, 2, 4, 4, 2],
           [3, 5, 1, 3, 1]]

moves_1 = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board_1, moves_1))

# 내 풀이 -> 틀림
def solution_error(board, moves):
    answer = 0

    # 바구니 리스트
    basket = []
    up_down_basket = []

    # Numpy의 array
    board_lst_to_arr = np.array(board).copy()

    for i in moves:
        machine_pick_row = board_lst_to_arr[:, i - 1]
        for j in machine_pick_row:
            if j != 0:
                basket.append(j)
                machine_pick_row[np.where(machine_pick_row == j)] = 0

            else:
                continue

            break

    # print(basket)


    # 첫 비교 값
    first = 0

    for i in basket:
        first = basket.pop(0)
        if i != first:
            up_down_basket.append(first)
            first = basket.pop(0)
        elif i == first:
            answer += 2
            basket.pop(0)
        elif up_down_basket[-1] == first:
            answer += 2
            up_down_basket.pop(-1)

    return answer

# print(solution_error(board_1, moves_1))

def solution_best(board, moves):
    answer = 0

    return answer

# print(solution_best(board_1, moves_1))

def solution_other(board, moves):
    answer = []

    # 바구니 리스트
    bucket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0

                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break

    return len(answer) * 2

# print(solution_other(board_1, moves_1))


