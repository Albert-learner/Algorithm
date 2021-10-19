# 15. 네트워크

'''
BFS(Breath-First Search를 이용한 그래프 탐색
'''
def solution(n, computers):
    answer = 0

    bfs = []
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        while bfs:
            first = bfs.pop(0)
            visited[first] = 1

            for i in range(n):
                if visited[i] == 0 and computers[first][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer

n_1 = 3
n_2 = 3

computers_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers_2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# print(solution(n_1, computers_1))
# print(solution(n_2, computers_2))

'''
DFS를 이용한 그래프 탐색
'''
def solution_other(n, computers):
    answer = 0

    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1

    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

# print(solution_other(n_1, computers_1))
# print(solution_other(n_2, computers_2))

'''
BFS 이용한 풀이
'''
from collections import deque

def solution_best(n, computers):
    def BFS(i):
        q = deque()
        q.append(i)

        while q:
            cst = q.popleft()
            visited[cst] = 1
            for a in range(n):
                if computers[cst][a] and not visited[a]:
                    q.append(a)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1

    return answer

# print(solution_best(n_1, computers_1))
# print(solution_best(n_2, computers_2))