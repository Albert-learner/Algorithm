# 1189. 컴백홈

"""
I didn't solve this problem by myself. This is about Back Tracking Algorithm.
The limitation is moving coordinate is '.'.
And DFS is better than BFS for applying Back Tracking.
See it again.
"""
# 1. My Solution(practice)
R, C, K = map(int, input().split())
road_map = [list(input()) for _ in range(R)]

ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
answer = 0

def DFS(x, y, distance):
    global answer
    if x == 0 and y == C - 1 and distance == K:
        answer += 1
    else:
        road_map[x][y] = 'T'
        for dx, dy in ds_dict.values():
            mx, my = x + dx, y + dy
            if mx in range(R) and my in range(C) and road_map[mx][my] == '.':
                road_map[mx][my] = 'T'
                DFS(mx, my, distance + 1)
                road_map[mx][my] = '.'

DFS(R - 1, 0, 1)
print(answer)

# 1. My Solution
R, C, K = map(int, input().split())
road_map = [list(input()) for _ in range(R)]

ds_dict = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

answer = 0
def DFS(x, y, distance):
    global answer
    if distance == K and x == 0 and y == C - 1:
        answer += 1
    else:
        road_map[x][y] = 'T'
        for dx, dy in ds_dict.values():
            mx, my = x + dx, y + dy

            if mx in range(R) and my in range(C) and road_map[mx][my] == '.':
                road_map[mx][my] = 'T'
                DFS(mx, my, distance + 1)
                road_map[mx][my] = '.'

DFS(R - 1, 0, 1)
print(answer)

# 2. Not my Solution
import sys
input = sys.stdin.readline

# r X c  맵
# 거리가 k 인 가짓수 구하기
r,c,k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 0
def dfs(x,y,distance):
    global answer
    # 목표 도착 지점 : (0,c-1)
    # 목표 거리 : k
    if distance == k and y == c-1 and x==0:
        answer += 1
    else:
        # T로 방문처리
        graph[x][y]='T'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 백트래킹 한정 조건 : graph[nx][ny] == '.'
            if(0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.'):
                graph[nx][ny]='T'
                dfs(nx,ny,distance+1)
                # 원래 상태로 돌려 놓아 다른 방향으로 다시 탐색하도록 한다.
                graph[nx][ny]='.'

# 시작점 : (r-1,0)
# 초기 distance : 1
dfs(r-1,0,1)
# 정답
print(answer)

"""
3 4 6
....
.T..
....
=>
4
"""