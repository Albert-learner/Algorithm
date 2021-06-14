# 41. 프렌즈4블록

# Not solve by myself.
def pop_num(b, m, n):
    pop_set = set()

    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])

    # set board
    for i, j in pop_set:
        b[i][j] = 0

    for row_idx, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[row_idx] = empty + [block for block in row if block != 0]

    return len(pop_set)

def solution(m, n, board):
    answer = 0

    game_board = list(map(list, zip(*board)))
    while True:
        pop = pop_num(game_board, m, n)
        if pop == 0: return answer
        answer += pop

    return answer

m_1 = 4
m_2 = 6

n_1 = 5
n_2 = 6

board_1 = ["CCBDE",
           "AAADE",
           "AAABF",
           "CCBBF"
           ]
board_2 = ["TTTANT",
           "RRFACC",
           "RRRFCC",
           "TRRRAA",
           "TTMMMF",
           "TMMTTJ"
           ]

print(solution(m_1, n_1, board_1))
print(solution(m_2, n_2, board_2))

'''
board를 3차원 리스트로 만들고
[ [['C'], ['C'], ['B'], ['D'], ['E']],
  [['A'], ['A'], ['A'], ['D'], ['E']],
  ...(이렇게 하면 안 됨)

len(board) - 1, len(board[0]) -1만큼 반복하면서
겹치는 부분을 0으로 초기화한 후

다시 반복하면서 값이 0인 경우 pop을 하는 방식으로 생각했는데
그럴 경우 pop이 안된다.
'''
def solution_mine(m, n, board):
    answer = 0

    game_board = [[[ch] for ch in row] for row in board]
    print(game_board)
    for row in range(len(game_board) - 1):
        for col in range(len(game_board[0]) - 1):
            if game_board[row][col] == game_board[row][col + 1] == \
                    game_board[row + 1][col] == game_board[row + 1][col + 1]:
                game_board[row][col], game_board[row][col + 1], \
                game_board[row + 1][col], game_board[row + 1][col + 1] \
                    = 0, 0, 0, 0

    for row in range(len(game_board) - 1):
        for col in range(len(game_board[0]) - 1):
            if row != 0 and col != 0:
                game_board[row][col], game_board[row][col + 1] = game_board[row - 1][col], game_board[row - 1][col + 1]
            else:
                game_board[row].pop(col)
                game_board[row].pop(col + 1)
                answer += 2
    return answer

# print(solution_mine(m_1, n_1, board_1))
# print(solution_mine(m_2, n_2, board_2))

def solution_other(m, n, board):
    answer = 0

    # board 배열로 만들기
    for i in range(len(board)):
        popped = board.pop(0)
        board.append([p for p in popped])

    # 터진 블록이 없을 때까지 반복
    while True:
        # 이번 턴에 터져야 할 블록들 모음
        checked = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '0':
                    continue

                # 연속으로 두 개가 동일한 블록이면, 밑에 두 개도 동일한지 확인
                if board[i][j] == board[i][j + 1]:
                    if board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]:
                        # 터져야 할 블록들 전부 저장
                        checked.append((i, j))
                        checked.append((i, j + 1))
                        checked.append((i + 1, j))
                        checked.append((i + 1, j + 1))

        # 이번에 터진 블록 없으면 종료
        if len(checked) == 0:
            break
        else:
            # 모아둔 블록 다 터뜨리기
            answer += len(set(checked))
            for c in checked:
                board[c[0]][c[1]] = '0'

            # 블록들 내리기
            for c in reversed(checked):
                check_n = c[0] - 1
                put_n = c[0]

                # 터진 자리 위에 있는 블록들 다 내린다다
                while check_n >= 0:
                    if board[put_n][c[1]] == '0' and board[check_n][c[1]] != "0":
                        board[put_n][c[1]] = board[check_n][c[1]]
                        board[check_n][c[1]] = "0"
                        put_n -= 1

                    check_n -= 1

    return answer

# print(solution_other(m_1, n_1, board_1))
# print(solution_other(m_2, n_2, board_2))

import numpy as np
def solution_best(m, n, board):
    list = []

    for i in board:
        for j in i:
            list.append(j)

    list = np.array(list).reshape(m, n)
    test = np.zeros((m, n))
    a = []

    while 1:  # 전체 코드 돌리는 for문
        for i in range(m):
            if i + 1 != len(list):
                for j in range(1, n):
                    if list[i][j - 1] == list[i][j] == list[i + 1][j] == list[i + 1][j - 1]:
                        if list[i][j - 1] == ' ' or list[i][j - 1] == '':
                            test[i][j - 1], test[i][j], test[i + 1][j], test[i + 1][j - 1] = '0' * 4
                        else:
                            test[i][j - 1], test[i][j], test[i + 1][j], test[i + 1][j - 1] = '1' * 4

        a.append(np.sum(test))
        r = np.sum(test)

        testwhere = np.where(test == 1)
        list[testwhere] = "@"

        for g in range(max(m, n)):
            for i in range(m):
                if i - 1 != -1:
                    for j in range(0, n):
                        if list[i][j] == '@' or list[i][j] == '':
                            if list[i - 1][j] is not None:
                                list[i][j] = list[i - 1][j]
                                list[i - 1][j] = ''

        test[testwhere] = 0

        if r == 0:
            answer = sum(a)
            return answer