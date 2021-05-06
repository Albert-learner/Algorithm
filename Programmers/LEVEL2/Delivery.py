# 28. 배달

# 최단 거리 알고리즘 문제 ... Dijkstra(구현을 못함)
from collections import deque
def solution(N, road, K):
    answer = 0

    nodes = {}
    dist = {i : float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    for frm, to, d in road:
        nodes[frm] = nodes.get(frm, []) + [(to, d)]
        nodes[to] = nodes.get(to, []) + [(frm, d)]

    que = deque([1])
    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    answer = len([True for dist in dist.values() if dist <= K])
    return answer

N_1 = 5
N_2 = 6

road_1 = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
road_2 = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]

K_1 = 3
K_2 = 4

print(solution(N_1, road_1, K_1))
print(solution(N_2, road_2, K_2))

import math

def bfs(start, maps, distance, K):
    que = deque()
    que.append(start)

    # 처음 출발한 도시의 distance = 0
    distance[start] = 0

    while que:
        y = que.popleft()
        for x in range(1, len(maps)):
            # 도착할 수 있는 도시인 경우
            if maps[y][x] != 0:
                '''해당 마을까지의 거리가 현재까지의 거리 + 이동할 때 걸리는 거리보다 작다.
                 현재까지의 거리 + 이동할 때의 거리가 K보다 작다'''
                if distance[x] > distance[y] + maps[y][x] and distance[y] + maps[y][x] <= K:
                    distance[x] = distance[y] + maps[y][x]
                    que.append(x)

    # distance 값 중 K보다 작은 값의 개수만 리턴
    return len([i for i in distance if i <= K])

def solution_other(N, road, K):
    '''시작지점 1에서부터 해당 마을까지의 거리.
       초기값을 inf로 설정하고, 계산한 거리가 distance[마을]보다 작으면 distance를
       업데이트해준다.'''
    distance = [math.inf for _ in range(N + 1)]

    # 그래프 그리기
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for frm, to, w in road:
        # 0이면 초기화한 값 그대로이므로 w값을 넣어준다
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            # 중복된 값이 있을 경우, 가장 작은 weight만 사용한다.
            if w < maps[frm][to]:
                maps[frm][to], maps[to][frm] = w, w

    return bfs(1, maps, distance, K)

# print(solution_other(N_1, road_1, K_1))
# print(solution_other(N_2, road_2, K_2))

def solution_best(N, road, K):
    answer = 0

    nodes = {}
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    que = deque([1])

    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    answer = len([True for dist in dist.values() if dist <= K])
    return answer

# print(solution_best(N_1, road_1, K_1))
# print(solution_best(N_2, road_2, K_2))