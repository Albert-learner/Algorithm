# Restart 38. 공원 산책

import copy
# My solution can't solve if obstacle is on my route
def solution_mine(park, routes):
    answer = []

    move_directions = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    board = [[elem for elem in row] for row in park]
    board_row, board_col = len(board), len(board[0])
    start_pos = [0, board[0].index('S')]

    for route in routes:
        direction, distance = route.split()[0], int(route.split()[1])
        moving_pos = [elem * distance for elem in move_directions[direction]]
        print('moving_pos :', moving_pos)
        if moving_pos[0] >= board_row - 1 or moving_pos[1] >= board_col - 1:
            continue

        changed_pos = [st_p + mo_p for st_p, mo_p in zip(start_pos, moving_pos)]
        print('changed_pos :', changed_pos)
        print(board[changed_pos[0]][changed_pos[1]])
        if board[changed_pos[0]][changed_pos[1]] == 'X':
            continue
        start_pos = copy.deepcopy(changed_pos)

    return answer

# This is wrong just only 4 test case.
def solution_other(park, routes):
    answer = []

    move_directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    board = [[elem for elem in row] for row in park]
    board_row, board_col = len(board) - 1, len(board[0]) - 1
    start_pos_x, start_pos_y = 0, 0
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 'S':
                start_pos_x, start_pos_y = row, col
                break
    # start_pos = (0, board[0].index('S'))

    for route in routes:
        direction, cnts = route.split()[0], int(route.split()[1])
        dx, dy = start_pos_x, start_pos_y

        for cnt in range(cnts):
            changed_pos_x, changed_pos_y = start_pos_x + move_directions[direction][0], start_pos_y + \
                                           move_directions[direction][1]

            if 0 <= changed_pos_x <= board_row and 0 <= changed_pos_y <= board_col and board[changed_pos_x][
                changed_pos_y] != 'X':
                start_pos_x, start_pos_y = changed_pos_x, changed_pos_y
            else:
                start_pos_x, start_pos_y = dx, dy
                break

    answer = [start_pos_x, start_pos_y]
    return answer

# Solve this problem not by myself
def solution(park, routes):
    move_directions = {'E': (0, 1), 'W': (0, -1),
                       'S': (1, 0), 'N': (-1, 0)}
    park_row, park_col = len(park), len(park[0])
    x, y = 0, 0
    for row in range(park_row):
        for col in range(park_col):
            if park[row][col] == 'S':
                x, y = row, col
                break
    # start_pos = (0, board[0].index('S'))

    for route in routes:
        direction, cnts = route.split()[0], int(route.split()[1])
        dx, dy = x, y

        for cnt in range(cnts):
            changed_pos_x, changed_pos_y = x + move_directions[direction][0], y + move_directions[direction][1]

            if 0 <= changed_pos_x <= park_row - 1 and 0 <= changed_pos_y <= park_col - 1 and park[changed_pos_x][
                changed_pos_y] != 'X':
                x, y = changed_pos_x, changed_pos_y
            else:
                x, y = dx, dy
                break

    return [x, y]


park_1 = ["SOO","OOO","OOO"]
park_2 = ["SOO","OXX","OOO"]
park_3 = ["OSO","OOO","OXO","OOO"]

routes_1 = ["E 2","S 2","W 1"]
routes_2 = ["E 2","S 2","W 1"]
routes_3 = ["E 2","S 3","W 1"]

# print(solution_mine(park_1, routes_1))
# print(solution_mine(park_2, routes_2))
# print(solution_mine(park_3, routes_3))
#
# print(solution_other(park_1, routes_1))
# print(solution_other(park_2, routes_2))
# print(solution_other(park_3, routes_3))

print(solution(park_1, routes_1))
print(solution(park_2, routes_2))
print(solution(park_3, routes_3))


