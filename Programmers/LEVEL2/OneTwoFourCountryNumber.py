# 5. 124 나라의 숫자

def solution(n):
    answer = ''

    if n <= 3:
        answer = '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        answer = solution(q) + '124'[r]
    return answer

n_1 = 1
n_2 = 2
n_3 = 3
n_4 = 4

# print(solution(n_1))
# print(solution(n_2))
# print(solution(n_3))
# print(solution(n_4))

def solution_other(n):
    answer = ''
    num = ['1', '2', '4']

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

print(solution_other(n_1))
print(solution_other(n_2))
print(solution_other(n_3))
print(solution_other(n_4))