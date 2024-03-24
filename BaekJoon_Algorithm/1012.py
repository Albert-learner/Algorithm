# 1012. 유기농 배추

"""
I didn't solve this problem by myself. This is about Search and BFS is better than DFS in this problem.
This is a basic BFS code, so I have to rewind the flow.
See it again.
"""
# 1. My Solution
T = int(input())

ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

def BFS(x, y):
    queue = [(x, y)]
    ground[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for dx, dy in ds_dict.values():
            mx, my = x + dx, y + dy

            if mx < 0 or mx >= M or my < 0 or my >= N:
                continue

            if ground[mx][my] == 1:
                queue.append((mx, my))
                ground[mx][my] = 0


for t in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * N for _ in range(M)]
    min_cnts = 0

    for k in range(K):
        x, y = map(int, input().split())
        ground[x][y] = 1

    for row in range(M):
        for col in range(N):
            if ground[row][col] == 1:
                BFS(row, col)
                min_cnts += 1

    print(min_cnts)


# # 2. Not my Solution
# T = int(input()) #테스트케이스의 개수
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def BFS(x,y):
#     queue = [(x,y)]
#     matrix[x][y] = 0 # 방문처리
#
#     while queue:
#         x,y = queue.pop(0)
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue
#
#             if matrix[nx][ny] == 1 :
#                 queue.append((nx,ny))
#                 matrix[nx][ny] = 0
#
# # 행렬만들기
# for i in range(T):
#     M, N, K = map(int, input().split())
#     matrix = [[0] * (N) for _ in range(M)]
#     cnt = 0
#
#     for j in range(K):
#         x,y = map(int, input().split())
#         matrix[x][y] = 1
#
#     for a in range(M):
#         for b in range(N):
#             if matrix[a][b] == 1:
#                 BFS(a, b)
#                 cnt += 1
#
#     print(cnt)


"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
=>
5
1
=======================
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
=>
2
"""