# 3. 삼각 달팽이

from itertools import chain

# 어렵다 ... 내 풀이 X
def solution(n):
    answer = []

    maps = [[0 for i in range(n)] for j in range(n)]
    y, x = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            maps[y][x] = num
            num += 1
    answer = [i for i in chain(*maps) if i != 0]
    return answer

n_1 = 4
n_2 = 5
n_3 = 6

print(solution(n_1))
print(solution(n_2))
print(solution(n_3))

# 다른 풀이
import itertools

def get_next(cur_y, cur_x, cur_d):
    DELTAS = {'U' : (-1, -1), 'D' : (1, 0), 'R' : (0, 1)}
    dy, dx = DELTAS[cur_d][0], DELTAS[cur_d][1]
    nxt_y, nxt_x = cur_y + dy, cur_x + dx

    return nxt_y, nxt_x

def check_turn(nxt_y, nxt_x, n, snail):
    return nxt_y < 0 or nxt_y >= n or nxt_x > nxt_y or snail[nxt_y][nxt_x] != 0

def solution_best(n):
    answer = []
    NEXT = {'U' : 'D', 'D' : 'R', 'R' : 'U'}
    N = sum(range(1, n + 1))
    snail = [[0] * i for i in range(1, n + 1)]

    cur_y, cur_x, cur_d = 0, 0, 'D'
    for num in range(1, N + 1):
        snail[cur_y][cur_x] = num
        if check_turn(*get_next(cur_y, cur_x, cur_d), n, snail):
            cur_d = NEXT[cur_d]
        cur_y, cur_x = get_next(cur_y, cur_x, cur_d)

    answer = list(itertools.chain(*snail))
    return answer

print(solution_best(n_1))
print(solution_best(n_2))
print(solution_best(n_3))