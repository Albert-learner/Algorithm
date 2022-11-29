# Restart 11. 삼각형의 완성조건 (2)

# My Solution
def solution(sides):
    sides.sort()
    answer = len(range(sides[1] - sides[0] + 1, sides[1] + 1)) + len(range(sides[1] + 1, sum(sides)))

    return answer

sides_1 = [1, 2]
sides_2 = [3, 6]
sides_3 = [11, 7]

print(solution(sides_1))
print(solution(sides_2))
print(solution(sides_3))

def solution_other(sides):
    answer = len(list(range(abs(sides[0] - sides[1]) + 1, sum(sides))))

    return answer

print(solution_other(sides_1))
print(solution_other(sides_2))
print(solution_other(sides_3))

def solution_best(sides):
    answer = sum(sides) - max(sides) + min(sides) - 1

    return answer

print(solution_best(sides_1))
print(solution_best(sides_2))
print(solution_best(sides_3))