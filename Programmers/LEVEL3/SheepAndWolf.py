# 33. 양과 늑대

def solution(info, edges):
    def NextNodes(v):
        tmp = []
        for edge in edges:
            parent, child = edge

            if v == parent:
                tmp.append(child)
        return tmp

    def DFS(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        
    return answer

info_1 = [0,0,1,1,1,0,1,0,1,0,1,1]
info_2 = [0,1,0,1,1,0,1,0,0,1,0]

edges_1 = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
edges_2 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info_1, edges_1))
print(solution(info_2, edges_2))


def DFS(sheep, wolf, current, path):
    if info[current]:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf:
        return 0

    max_sheep = sheep

    for p in path:
        for n in NextNodes(p):
            if n not in path:
                path.append(n)
                max_sheep = max(max_sheep, DFS(sheep, wolf, n, path))
                path.pop()

    return max_sheep


answer = DFS(0, 0, 0, [0])

def solution_other(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1

    def DFS(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                DFS(sheep + (isWolf == 0), wolf + (isWolf == 1))
                visited[child] = 0

    DFS(1, 0)
    answer = max(answer)
    return answer

print(solution_other(info_1, edges_1))
print(solution_other(info_2, edges_2))

