# 37. 예산

def solution(d, budget):
    answer = 0

    # 총 가능 금액
    total = 0

    d.sort()
    for i in d:
        if total + i <= budget:
            total += i
            answer += 1
        else:
            break
    return answer

d_1 = [1, 3, 2, 5, 4]
d_2 = [2, 2, 3, 3]

budget_1 = 9
budget_2 = 10

print(solution(d_1, budget_1))
print(solution(d_2, budget_2))

def solution_best(d, budget):
    answer = 0

    d.sort()
    while budget < sum(d):
        d.pop()
    answer = len(d)
    return answer

print(solution_best(d_1, budget_1))
print(solution_best(d_2, budget_2))