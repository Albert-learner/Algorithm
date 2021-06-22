# 44. 게임 맵 최단 거리

def solution(maps):
    # 상대 팀 진영에 도착할 수 없는 경우
    answer = -1

    # 게임 맵 크기
    game_map_size = len(maps) - 1
    # 사용자 맵의 크기
    map_size = len(maps[0]) - 1
    # 이동방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 경로 저장 리스트
    path_lst = []

    # 게임 시작 위치, 1부터 시작
    path_lst.append([0, 0, 1])

    while path_lst:
        # 현재 위치
        x, y, cnt = path_lst.pop(0)
        # 지나온 길 벽으로 없애기
        maps[x][y] = 0
        # 너비 우선 탐색, 상하좌우
        for dx, dy in directions:
            mx, my = x + dx, y + dy
            # 마지막 지점 먼저 도달하면 경로 출력
            if mx == game_map_size and my == map_size:
                answer = cnt + 1
                return answer

            if 0 <= mx <= game_map_size and 0 <= my <= map_size and maps[mx][my] == 1:
                maps[mx][my] = 0
                path_lst.append([mx, my, cnt + 1])

    return answer

maps_1 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1],
          [0, 0, 0, 0, 1]
          ]
maps_2 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1]
          ]

print(solution(maps_1))
print(solution(maps_2))

'''
deque 사용하여 BFS로 해결하기
'''
from collections import  deque

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def solution_other(maps):
    rows = len(maps)
    cols = len(maps[0])
    table = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append([0, 0])
    table[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if -1 < ny < rows and -1 < nx < cols:
                if maps[ny][nx] == 1:
                    if table[ny][nx] == -1:
                        table[ny][nx] = table[y][x] + 1
                        queue.append([ny, nx])

    answer = table[-1][-1]
    return answer

maps_1 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1],
          [0, 0, 0, 0, 1]
          ]
maps_2 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1]
          ]
# print(solution_other(maps_1))
# print(solution_other(maps_2))

'''
위의 solution풀이와 비슷, deque 사용
'''
def solution_good(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    rows = len(maps)
    cols = len(maps[0])

    graph = [[-1 for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= my < rows and 0 <= mx < cols and maps[my][mx] == 1:
                if graph[my][mx] == -1:
                    graph[my][mx] = graph[y][x] + 1
                    queue.append([my, mx])

    answer = graph[-1][-1]

    return answer

maps_1 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1],
          [0, 0, 0, 0, 1]
          ]
maps_2 = [[1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1]
          ]
# print(solution_good(maps_1))
# print(solution_good(maps_2))