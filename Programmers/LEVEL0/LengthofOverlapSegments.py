# Restart 25. 겹치는 선분의 길이

def solution(lines):
    answer = 0

    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index)

    for line in table:
        if len(line) > 1:
            answer += 1
    return answer

lines_1 = [[0, 1], [2, 5], [3, 9]]
lines_2 = [[-1, 1], [1, 3], [3, 9]]
lines_3 = [[0, 5], [3, 9], [1, 10]]

print(solution(lines_1))
print(solution(lines_2))
print(solution(lines_3))

def solution_best(lines):
    answer = 0

    sets = [set(range(min(line), max(line))) for line in lines]
    answer = len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    return answer

print(solution_best(lines_1))
print(solution_best(lines_2))
print(solution_best(lines_3))