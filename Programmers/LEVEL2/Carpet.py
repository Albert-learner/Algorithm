# 18. 카펫

def solution(brown, yellow):
    answer = []

    total = brown + yellow
    for i in range(total, 2, -1):
        if total % i == 0:
            height = total // i
            if yellow == (i - 2) * (height - 2):
                answer = [i, height]
                return answer
    return answer

brown_1 = 10
brown_2 = 8
brown_3 = 24

yellow_1 = 2
yellow_2 = 1
yellow_3 = 24

print(solution(brown_1, yellow_1))
print(solution(brown_2, yellow_2))
print(solution(brown_3, yellow_3))

def solution_best(brown, yellow):
    x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + yellow)) ** 0.5) / 4
    y = (brown + yellow) // x

    return [int(max(x, y)), int(min(x, y))]

print(solution_best(brown_1, yellow_1))
print(solution_best(brown_2, yellow_2))
print(solution_best(brown_3, yellow_3))