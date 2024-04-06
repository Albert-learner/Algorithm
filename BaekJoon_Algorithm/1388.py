# 1388. 바닥 장식

"""
I didn't solve this problem by myself. The key of this problem is DFS.
This is a basic implementation of DFS Algorithm. And this can be solved without using DFS Algorithm.
See two methods again.
"""
# 1. My Solution(practice, DFS)
N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]

def DFS(x, y):
    if floor[x][y] == '-':
        floor[x][y] = 1
        for _y in [-1, 1]:
            ran_y = y + _y
            if 0 <= ran_y < M and floor[x][ran_y] == '-':
                DFS(x, ran_y)

    if floor[x][y] == '|':
        floor[x][y] = 1
        for _x in [-1, 1]:
            ran_x = x + _x
            if 0 <= ran_x < N and floor[ran_x][y] == '|':
                DFS(ran_x, y)

cnts = 0
for row in range(N):
    for col in range(M):
        if floor[row][col] == '-' or floor[row][col] == '|':
            DFS(row, col)
            cnts += 1

print(cnts)

# 2. My Solution(Practice, not DFS)
N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]

cnts = 0
for row in range(N):
    a = ""
    for col in range(M):
        if floor[row][col] == '-':
            if floor[row][col] != a:
                cnts += 1

        a = floor[row][col]

for col in range(M):
    a = ""
    for row in range(N):
        if floor[row][col] == '|':
            if floor[row][col] != a:
                cnts += 1

        a = floor[row][col]

print(cnts)

# 1388. 바닥 장식

# 1. My Solution
N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]

def DFS(x, y):
    if floor[x][y] == '-':
        floor[x][y] = 1
        for _y in [-1, 1]:
            ran_y = y + _y
            if (0 < ran_y < M) and floor[x][ran_y] == '-':
                DFS(x, ran_y)

    if floor[x][y] == '|':
        floor[x][y] = 1
        for _x in [-1, 1]:
            ran_x = x + _x
            if (0 < ran_x < N) and floor[ran_x][y] == '|':
                DFS(ran_x, y)

cnts = 0
for row in range(N):
    for col in range(M):
        if floor[row][col] == '-' or floor[row][col] == '|':
            DFS(row, col)
            cnts += 1

print(cnts)

# # 2. Not my Solution(Blog, DFS)
# # dfs 알고리즘 함수 정의
# def dfs(x, y):
#     # 바닥 장식 모양이 '-' 일 때
#     if graph[x][y] == '-':
#         graph[x][y] = 1  # 해당 노드 방문처리
#         for _y in [1, -1]:  # 양옆(좌우) 확인하기
#             Y = y + _y
#             # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
#             if (Y > 0 and Y < m) and graph[x][Y] == '-':
#                 dfs(x, Y)
#     # 바닥 장식 모양이 '|' 일 때
#     if graph[x][y] == '|':
#         graph[x][y] = 1  # 해당 노드 방문처리
#         for _x in [1, -1]:  # 상하(위아래) 확인하기
#             X = x + _x
#             # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
#             if (X > 0 and X < n) and graph[X][y] == '|':
#                 dfs(X, y)
#
#
# n, m = map(int, input().split())  # 방 바닥의 세로 크기 n, 가로 크기 m
# graph = []  # 2차원 리스트의 맵 정보 저장할 공간
# for _ in range(n):
#     graph.append(list(input()))
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == '-' or graph[i][j] == '|':
#             dfs(i, j)  # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
#             count += 1
#
# print(count)

# # 3. Not my Solution(Blog, not DFS)
# # 방 바닥의 세로 크기 n, 가로 크기 m
# n, m = map(int, input().split())
# graph = []  # 2차원 리스트의 맵 정보 저장할 공간
# for _ in range(n):
#     graph.append(list(input()))
#
# # '-'모양의 나무 판자 개수 계산
# count = 0
# for i in range(n):
#     a = ''
#     for j in range(m):
#         if graph[i][j] == '-':
#             if graph[i][j] != a:
#                 count += 1
#         a = graph[i][j]
#
# # 'ㅣ'모양의 나무 판자 개수 계산
# for j in range(m):
#     a = ''
#     for i in range(n):
#         if graph[i][j] == '|':
#             if graph[i][j] != a:
#                 count += 1
#         a = graph[i][j]
#
# print(count)

"""
4 4
----
----
----
----
=>
4
============
6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-
=>
31
============
7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------
=>
13
============
10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||
=>
41
=============
6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-
=>
19
"""