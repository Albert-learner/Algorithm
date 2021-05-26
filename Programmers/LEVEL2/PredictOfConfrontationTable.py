# 37. 예상 대진표


def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer

n_1 = 8

a_1 = 4

b_1 = 7

print(solution(n_1, a_1, b_1))

def solution_best(n, a, b):
    answer = ((a - 1) ^ (b - 1)).bit_length()

    return answer

print(solution_best(n_1, a_1, b_1))