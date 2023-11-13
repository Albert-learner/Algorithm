# 삼성 SW 역량 기출문제 1. 구슬 탈출 2
from collections import deque

import sys
# Fast input Output
input = sys.stdin.readline

board_row, board_col = map(int, input().split())

board = [[elem for elem in input()] for row in range(board_row)]
# print(board)

visited = [[[[False] * board_col for _ in range(board_row)] for _ in range(board_col)] for _ in range(board_row)]
# print(visited)
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
que = deque()

# Save Red Blade position and Blue Blade position
def init():
    rx, ry, bx, by = [0] * 4
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 'R':
                rx, ry = row, col
            elif board[row][col] == 'B':
                bx, by = row, col

    que.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

# Move function that if next movement is wall or hole
def move(x, y, dx, dy):
    move_cnts = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_cnts += 1

    return x, y, move_cnts

# Use BFS(Breath-First Search) to find the answer
def BFS():
    init()
    while que:
        rx, ry, bx, by, depth = que.popleft()
        if depth > 10:
            break

        # Search for Four directions
        for four_dir in range(len(dx)):
            next_rx, next_ry, r_cnt = move(rx, ry, dx[four_dir], dy[four_dir])
            next_bx, next_by, b_cnt = move(bx, by, dx[four_dir], dy[four_dir])

            # If Blue Blade in hole, it's not the end(failure)
            if board[next_bx][next_by] == 'O':
                continue

            if board[next_rx][next_ry] == 'O':
                print(depth)
                return

            # Except cases that Red Blade and Blue Blade are in same position
            if next_rx == next_bx and next_ry == next_by:
                # Move Blade back that move counts are more than another one
                if r_cnt > b_cnt:
                    next_rx -= dx[four_dir]
                    next_ry  -= dy[four_dir]
                else:
                    next_bx -= dx[four_dir]
                    next_by -= dy[four_dir]

            # Finished BFS and check visited
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                que.append((next_rx, next_ry, next_bx, next_by, depth + 1))

    print(-1)

BFS()

'''
board_1 :
#####
#..B#
#.#.#
#RO.#
#####

board_2 :
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

board_3 :
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######

board_4 :
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########

board_5 :
#######
#R.O.B#
#######

board_6 :
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########

board_7 :
##########
#.O....RB#
##########
'''