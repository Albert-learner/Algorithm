# 20. 약수의 합

def solution(n):
    answer = 0

    # 약수 저장 리스트
    aliquot_lst = []

    for i in range(1, n + 1):
        if n % i == 0:
            aliquot_lst.append(i)

    answer = sum(aliquot_lst)
    return answer

n_1 = 12
n_2 = 5

print(solution(n_1))
print(solution(n_2))

def solution_best(n):
    answer = n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

    return answer

print(solution_best(n_1))
print(solution_best(n_2))