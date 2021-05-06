# 36. x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []

    for i in range(1, n + 1):
        answer.append(x * i)
    return answer

x_1 = 2
x_2 = 4
x_3 = -4

n_1 = 5
n_2 = 3
n_3 = 2

print(solution(x_1, n_1))
print(solution(x_2, n_2))
print(solution(x_3, n_3))

def solution_best(x, n):
    answer = [i * x for i in range(1, n + 1)]

    return answer

print(solution_best(x_1, n_1))
print(solution_best(x_2, n_2))
print(solution_best(x_3, n_3))