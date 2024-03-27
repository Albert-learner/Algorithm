# 1260. DFS와 BFS

"""
I didn't solve this problem by myself. This is a fundamental concept of DFS and BFS.
And there are two versions of applying BFS and DFS(Bi-directional vertex and vertex).
See it again.
"""
# 1. My Solution(practice)
from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = True
    graph[end][start] = True

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

def DFS(moving_v):
    dfs_visited[moving_v] = True
    print(moving_v, end=' ')

    for i in range(1, N + 1):
        if not dfs_visited[i] and graph[moving_v][i]:
            DFS(i)

def BFS(moving_v):
    v_que = deque([moving_v])
    bfs_visited[moving_v] = True

    while v_que:
        moving_v = v_que.popleft()
        print(moving_v, end=' ')
        for i in range(1, N + 1):
            if not bfs_visited[i] and graph[moving_v][i]:
                v_que.append(i)
                bfs_visited[i] = True

DFS(V)
print()
BFS(V)

# # 1. My Solution(Reference code)
# from collections import deque
# N, M, V = map(int, input().split())
# graph = [[False] * (N + 1) for _ in range(N + 1)]
#
# for _ in range(N):
#     start, end = map(int, input().split())
#     graph[start][end] = True
#     graph[end][start] = True
#
# dfs_visited = [False] * (N + 1)
# bfs_visited = [False] * (N + 1)
#
# def DFS(moving_v):
#     dfs_visited[moving_v] = True
#     print(moving_v, end=' ')
#     for i in range(1, N + 1):
#         if not dfs_visited[i] and graph[moving_v][i]:
#             DFS(i)
#
# def BFS(moving_v):
#     v_que = deque([moving_v])
#     bfs_visited[moving_v] = True
#
#     while v_que:
#         moving_v = v_que.popleft()
#         print(moving_v, end=' ')
#         for i in range(1, N + 1):
#             if not bfs_visited[i] and graph[moving_v][i]:
#                 v_que.append(i)
#                 bfs_visited[i] = True
#
# DFS(V)
# print()
# BFS(V)

# 2. Not my Solution
from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

def DFS(moving_v):
    dfs_visited[moving_v] = True
    print(moving_v, end=' ')
    for i in graph[moving_v]:
        if not dfs_visited[i]:
            DFS(i)

def BFS(moving_v):
    v_que = deque([moving_v])
    bfs_visited[moving_v] = True

    while v_que:
        moving_v = v_que.popleft()
        print(moving_v, end=' ')
        for i in graph[moving_v]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                v_que.append(i)


DFS(V)
print()
BFS(V)
"""
4 5 1
1 2
1 3
1 4
2 4
3 4
=>
1 2 4 3
1 2 3 4
==============
5 5 3
5 4
5 2
1 2
3 4
3 1
=>
3 1 2 5 4
3 1 4 2 5
==============
1000 1 1000
999 1000
=>
1000 999
1000 999
"""