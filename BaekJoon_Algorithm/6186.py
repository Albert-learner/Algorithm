# 6186. Best Grass

"""
I didn't solve this problem by myself. The key of this problem is BFS and DFS.
This is a basic problem of solving both BFS and DFS. But BFS is more efficient than using DFS.
See this again.
"""
# 1. My Solution(Practice, BFS)
from collections import deque

R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

def BFS(x, y):
    que = deque([(x, y)])
    field[x][y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in ds_dict.values():
            mx, my = x + dx, y + dy
            if 0 <= mx < R and 0 <= my < C and field[mx][my] == '#':
                que.append((mx, my))
                field[mx][my] = 1

cnts = 0
for row in range(R):
    for col in range(C):
        if field[row][col] == '#':
            BFS(row, col)
            cnts += 1

print(cnts)

# 2. My Solution(Practice, DFS)
import sys
sys.setrecursionlimit(100000)

R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
visited = [[False] * C for _ in range(R)]

def DFS(x, y):
    visited[x][y] = True
    for dx, dy in ds_dict.values():
        mx, my = x + dx, y + dy
        if 0 <= mx < R and 0 <= my < C and  field[mx][my] == '#' and not visited[mx][my]:
            DFS(mx, my)

cnts = 0
for row in range(R):
    for col in range(C):
        if field[row][col] == '#' and not visited[row][col]:
            DFS(row, col)
            cnts += 1

print(cnts)

# 6186. Best Grass

# 1. My Solution(BFS)
from collections import deque

R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
cnts = 0

def BFS(x, y):
    que = deque([(x, y)])
    field[x][y] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in ds_dict.values():
            mx, my = x + dx, y + dy
            if (0 <= mx < R) and (0 <= my < C) and field[mx][my] == '#':
                que.append((mx, my))
                field[mx][my] = 1

for row in range(R):
    for col in range(C):
        if field[row][col] == '#':
            BFS(row, col)
            cnts += 1

print(cnts)

# 2. My Solution(DFS)
import sys

sys.setrecursionlimit(100000)


R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

def DFS(x, y):
    visited[x][y] = True
    for dx, dy in ds_dict.values():
        mx, my = x + dx, y + dy
        if 0 <= mx < R and 0 <= my < C:
             if field[mx][my] == '#' and not visited[mx][my]:
                 DFS(mx, my)

cnts = 0
for row in range(R):
    for col in range(C):
        if field[row][col] == '#' and not visited[row][col]:
            DFS(row, col)
            cnts += 1

print(cnts)

# # 2. Not my Solution(Blog, BFS)
# from collections import deque
#
# def bfs(y, x):
#     q = deque()
#     q.append((y, x))
#     graph[y][x] = '1'
#     while q:
#         y, x = q.popleft()
#         for dy, dx in d:
#             Y, X = y+dy, x+dx
#             if (0 <= Y < R) and (0 <= X < C) and graph[Y][X] == '#':
#                 q.append((Y, X))
#                 graph[Y][X] = '1'
#
# R, C = map(int, input().split())
# graph = [list(input()) for _ in range(R)]
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# cnt = 0
# for i in range(R):
#     for j in range(C):
#         if graph[i][j] == '#':
#             bfs(i, j)
#             cnt += 1
# print(cnt)

# # 3. Not my Solution(Blog, DFS)
# import sys
#
# sys.setrecursionlimit(100000)
#
#
# def read():
#     return sys.stdin.readline().rstrip()
#
#
# vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# r, c = [int(i) for i in read().split(" ")]
# field = [[0 for _ in range(c)] for _ in range(r)]
# check = [[0 for _ in range(c)] for _ in range(r)]
# for i in range(r):
#     for j, char in enumerate(read()):
#         if char == '#':
#             field[i][j] = 1
#
#
# def dfs(y, x):
#     check[y][x] = 1
#     for dv in vec:
#         ny, nx = y + dv[0], x + dv[1]
#         range_chk = 0 <= ny < r and 0 <= nx < c
#         if range_chk:
#             if field[ny][nx] and not check[ny][nx]:
#                 dfs(ny, nx)
#
#
# ans = 0
# for y in range(r):
#     for x in range(c):
#         if field[y][x] and not check[y][x]:
#             dfs(y, x)
#             ans += 1
#
# print(ans)
"""
5 6
.#....
..#...
..#..#
...##.
.#....
=>
5
"""