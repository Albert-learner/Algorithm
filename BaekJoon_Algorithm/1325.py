# 1325. 효율적인 해킹

"""
I didn't solve this problem by myself. I think this is related with DFS.
But it's wrong for memory excess. So this is about BFS.
I need to see more about BFS implementation.
See it again.
"""
# 1. My Solution(practice)
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_conntections = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[end].append(start)

def BFS(moving_v):
    v_que = deque([moving_v])
    visited = [0] * (N + 1)
    visited[moving_v] = 1
    cnt = 1

    while v_que:
        moving_v = v_que.popleft()
        for connect in graph[moving_v]:
            if not visited[connect]:
                v_que.append(connect)
                visited[connect] = 1
                cnt += 1

    return cnt

max_cnt = 1
for i in range(1, N + 1):
    cnt = BFS(i)

    if cnt > max_cnt:
        max_cnt = cnt
        max_conntections = []
        max_conntections.append(i)
    elif cnt == max_cnt:
        max_conntections.append(i)

print(*max_conntections)

# 1325. 효율적인 해킹

# 1. My Solution
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_connections = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[end].append(start)

def BFS(moving_v):
    v_que = deque([moving_v])
    visited = [0] * (N + 1)
    visited[moving_v] = 1
    cnt = 1

    while v_que:
        v = v_que.popleft()
        for j in graph[v]:
            if not visited[j]:
                v_que.append(j)
                visited[j] = 1
                cnt += 1

    return cnt

max_cnt = 1
for i in range(1, N + 1):
    cnt = BFS(i)

    if cnt > max_cnt:
        max_cnt = cnt
        max_connections = []
        max_connections.append(i)
    elif cnt == max_cnt:
        max_connections.append(i)

print(*max_connections)

# 2. Not my Solution
import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
ret = []

for _ in range(m):
   a, b = map(int, input().split())
   g[b].append(a)

def dfs(i):
   global cnt
   visit[i] = 1
   for c in g[i]:
      if not visit[c]:
         cnt += 1
         dfs(c)

max_cnt = 0
for i in range(1, n + 1):
   visit = [0] * (n + 1)
   cnt = 1
   dfs(i)
   if cnt > max_cnt:
      max_cnt = cnt
      ret = []
      ret.append(i)
   elif cnt == max_cnt:
      ret.append(i)

print(*ret)
"""
5 4
3 1
3 2
4 3
5 3
=>
1 2
"""
"""
5 4
3 1
3 2
4 3
5 3
=>
1 2
"""