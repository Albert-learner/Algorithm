# 58. 피보나치 수

def solution(n):
    answer = 0

    fibo_lst = [0, 1]
    while len(fibo_lst) <= n:
        first, second = fibo_lst[-2], fibo_lst[-1]
        fibo_lst.append(first + second)

    answer = fibo_lst[-1] % 1234567
    return answer

n_1 = 3
n_2 = 5

print(solution(n_1))
print(solution(n_2))

def solution_other(n):
    answer = 0

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    answer = a % 1234567
    return answer

print(solution_other(n_1))
print(solution_other(n_2))