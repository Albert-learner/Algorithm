# 1446. 지름길

"""
I didn't solve this problem by myself. The key of this problem is Dijkstra Algorithm.
This problem can solve without Dijkstra, So I need to rewind two methods.
See it again.
"""
# 1. My Solution(practice, dijkstra)
import heapq as hq

def Dijkstra(start):
    dists_que = []
    hq.heappush(dists_que, (0, start))
    distances[start] = 0

    while dists_que:
        distance, cur_pos = hq.heappop(dists_que)

        if distance > distances[cur_pos]:
            continue

        for nxt_end, nxt_distance in shortcuts[cur_pos]:
            cost = distance + nxt_distance
            if cost < distances[nxt_end]:
                distances[nxt_end] = cost
                hq.heappush(dists_que, (cost, nxt_end))

N, D = map(int, input().split())
shortcuts = [[] for _ in range(D + 1)]
distances = [float("inf")] * (D + 1)

for pos in range(D):
    shortcuts[pos].append((pos + 1, 1))

for _ in range(N):
    start, end, distance = map(int, input().split())
    if end > D:
        continue

    shortcuts[start].append((end, distance))

Dijkstra(0)
print(distances[D])

# 2. My Solution(practice, no dijkstra)
N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

distances = [dist for dist in range(D + 1)]

for pos in range(D + 1):
    distances[pos] = min(distances[pos], distances[pos - 1] + 1)
    for start, end, distance in shortcuts:
        if pos == start and end <= D and distances[pos] + distance < distances[end]:
            distances[end] = distances[start] + distance

print(distances[D])

# # 2. Not my Solution(blog, Dijkstra)
# import heapq as hq
# INF = int(1e9)
#
# def Dijkstra(start):
#     dists_que = []
#     hq.heappush(dists_que, (0, start))
#     distances[start] = 0
#
#     while dists_que:
#         distance, cur_pos = hq.heappop(dists_que)
#
#         if distance > distances[cur_pos]:
#             continue
#
#         for nxt_end, nxt_distance in shortcuts[cur_pos]:
#             cost = distance + nxt_distance
#             if cost < distances[nxt_end]:
#                 distances[nxt_end] = cost
#                 hq.heappush(dists_que, (cost, nxt_end))
#
# N, D = map(int, input().split())
# shortcuts = [[] for _ in range(D + 1)]
# distances = [INF] * (D + 1)
#
# for pos in range(D):
#     shortcuts[pos].append((pos + 1, 1))
#
# for _ in range(N):
#     start, end, distance = map(int, input().split())
#     if end > D:
#         continue
#
#     shortcuts[start].append((end, distance))
#
# Dijkstra(0)
# print(distances[D])

# # 2. Not my Solution(blog, not Dijkstra)
# import heapq
# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#
#         #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
#         if dist > distance[now]:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost, i[0]))
#
#
# n , d = map(int,input().split())
# graph = [[] for _ in range(d+1)]
# distance = [INF] * (d+1)
#
# #일단 거리 1로 초기화.
# for i in range(d):
#     graph[i].append((i+1, 1))
#
# #지름길 있는 경우에 업데이트
# for _ in range(n):
#     s, e, l = map(int,input().split())
#     if e > d:# 고려 안해도 됨.
#         continue
#     graph[s].append((e,l))
#
# dijkstra(0)
# print(distance[d])

# 3. Not my solution
n, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

distances = [i for i in range(d + 1)]

for i in range(d + 1):
    distances[i] = min(distances[i], distances[i - 1] + 1)
    for start, end, distance in graph:
        if i == start and end <= d and distances[i] + distance < distances[end]:
            distances[end] = distances[start] + distance

print(distances[d])

"""
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
=>
70
=====================
2 100
10 60 40
50 90 20
=>
80
=====================
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
=>
432
"""