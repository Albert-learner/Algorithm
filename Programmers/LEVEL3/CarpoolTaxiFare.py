# 23. 합승 택시 요금

# Dijkstra
from math import inf
import heapq
def dijkstra(n, graph, start):
    dist = [inf for _ in range(n)]
    dist[start] = 0

    q = []
    heapq.heappush(q, [dist[start], start])
    while q:
        cur_dist, cur_dest = heapq.heappop(q)
        if dist[cur_dest] >= cur_dist:
            for i in range(n):
                new_dist = cur_dist + graph[cur_dest][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    heapq.heappush(q, [new_dist, i])

    return dist

def solution(n, s, a, b, fares):
    answer = inf

    s, a, b = s - 1, a - 1, b - 1
    graph = [[inf] * n for _ in range(n)]
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))

    for k in range(n):
        answer = min(answer, min_graph[s][k] + min_graph[k][a] + min_graph[k][b])

    return answer

n_1 = 6
n_2 = 7
n_3 = 6

s_1 = 4
s_2 = 3
s_3 = 4

a_1 = 6
a_2 = 4
a_3 = 5

b_1 = 2
b_2 = 1
b_3 = 6

fares_1 = [[4, 1, 10],
           [3, 5, 24],
           [5, 6, 2],
           [3, 1, 41],
           [5, 1, 24],
           [4, 6, 50],
           [2, 4, 66],
           [2, 3, 22],
           [1, 6, 25]]
fares_2 = [[5, 7, 9],
           [4, 6, 4],
           [3, 6, 1],
           [3, 2, 3],
           [2, 1, 6]]
fares_3 = [[2, 6, 6],
           [6, 3, 7],
           [4, 6, 7],
           [6, 5, 11],
           [2, 5, 12],
           [5, 3, 20],
           [2, 4, 8],
           [4, 3, 9]]

print(solution(n_1, s_1, a_1, b_1, fares_1))
print(solution(n_2, s_2, a_2, b_2, fares_2))
print(solution(n_3, s_3, a_3, b_3, fares_3))

# Floyd warshall
def solution_other(n, s, a, b, fares):
    answer = inf

    s, a, b = s - 1, a - 1, b - 1
    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for k in range(n):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer

print(solution_other(n_1, s_1, a_1, b_1, fares_1))
print(solution_other(n_2, s_2, a_2, b_2, fares_2))
print(solution_other(n_3, s_3, a_3, b_3, fares_3))

def solution_best(n, s, a, b, fares):
    answer = 987654321

    link = [[] for _ in range(n + 1)]
    for x, y, z in fares:
        link[x].append((z, y))
        link[y].append((z, x))

    def dijkstra(start):
        dist = [987654321] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))

        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    for i in range(1, n + 1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer

print(solution_best(n_1, s_1, a_1, b_1, fares_1))
print(solution_best(n_2, s_2, a_2, b_2, fares_2))
print(solution_best(n_3, s_3, a_3, b_3, fares_3))