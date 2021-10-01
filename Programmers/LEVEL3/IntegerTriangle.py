# 14. 정수 삼각형

def solution(triangle):
    answer = 0

    for rows in range(1, len(triangle)):
        for idx in range(rows + 1):
            if idx == 0:
                triangle[rows][idx] += triangle[rows - 1][idx]
            elif idx == rows:
                triangle[rows][idx] += triangle[rows - 1][-1]
            else:
                triangle[rows][idx] += max(triangle[rows - 1][idx - 1],
                                           triangle[rows - 1][idx])

    answer = max(triangle[-1])
    return answer

triangle_1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle_1))

def solution_other(triangle):
    answer = 0

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height - 2][i] += max([triangle[height - 1][i],
                                            triangle[height - 1][i + 1]])
        height -= 1

    answer = triangle[0][0]
    return answer

triangle_1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution_other(triangle_1))

solution_best = lambda t, l = []: max(l) if not t \
    else solution_best(t[1:], [max(x, y) + z for x, y, z in zip([0] + l,
                                                                l + [0],
                                                                t[0])])

triangle_1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution_best(triangle_1))