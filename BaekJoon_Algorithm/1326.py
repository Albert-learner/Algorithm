# 1326. 폴짝폴짝

"""
I didn't solve this problem by myself. The key of this problem is BFS.
I need to try implementing BFS even if it's hard.
See it again.
"""
# 1. My Solution(practice)
from collections import deque

def BFS(start, end, bridge, N):
    min_cnts = [float("inf")] * N
    poses_que = deque([start - 1])
    min_cnts[start - 1] = 0

    while poses_que:
        cur_pos = poses_que.popleft()
        for mov_pos in range(N):
            if (mov_pos - cur_pos) % bridge[cur_pos] == 0 and min_cnts[mov_pos] == float("inf"):
                poses_que.append(mov_pos)
                min_cnts[mov_pos] = min_cnts[cur_pos] + 1
                if mov_pos == end - 1:
                    return min_cnts[mov_pos]

    return -1

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

print(BFS(a, b, bridge, N))

# 1326. 폴짝폴짝

# 1. My Solution
from collections import deque

def BFS(start, end, bridge, N):
    poses_que = deque([start - 1])
    min_cnts = [-1] * N
    min_cnts[start - 1] = 0

    while poses_que:
        cur_pos = poses_que.popleft()
        for mov_pos in range(N):
            if (mov_pos - cur_pos) % bridge[cur_pos] == 0 and min_cnts[mov_pos] == -1:
                poses_que.append(mov_pos)
                min_cnts[mov_pos] = min_cnts[cur_pos] + 1
                if mov_pos == end - 1:
                    return min_cnts[mov_pos]

    return -1

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

print(BFS(a, b, bridge, N))

# # 1. My Solution(ChatGPT, wrong)
# from collections import deque
#
# def bfs(start, end, graph):
#     visited = [False] * (N + 1)
#     queue = deque([(start, 0)])  # (node, steps)
#     visited[start] = True
#
#     while queue:
#         node, steps = queue.popleft()
#
#         if node == end:
#             return steps
#
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append((neighbor, steps + 1))
#
#     return -1  # If destination is unreachable
#
# N = int(input())
# bridge = list(map(int, input().split()))
# a, b = map(int, input().split())
#
# graph = [[] for _ in range(N + 1)]
# for idx, pos in enumerate(bridge, start=1):
#     time = 1
#     while pos * time <= N:
#         graph[idx].append(pos * time)
#         time += 1
#
# min_steps = bfs(a, b, graph)
# print(min_steps)

# # 2. Not my Solution
# from collections import deque
#
# def bfs(a, b, bridge, N):
#     q = deque()
#     q.append(a-1)
#     check = [-1]*N
#     check[a-1] = 0
#     while q:
#         node = q.popleft()
#         for n in range(N):
#             if (n-node)%bridge[node] == 0 and check[n] == -1:
#                 q.append(n)
#                 check[n] = check[node] + 1
#                 if n == b-1:
#                     return check[n]
#     return -1
#
# N = int(input())
# bridge = list(map(int, input().split()))
# a, b = map(int, input().split())
# print(bfs(a, b, bridge, N))

"""
5
1 2 2 1 2
1 5
=>
1
"""