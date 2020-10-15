# 18. 수박수박수박수박수박수?

def solution(n):
    answer = ''

    if n == 1:
        answer = '수'
    elif n == 2:
        answer = '수박'
    else:
        answer += '수박'
        if n % 2 == 0:
            answer += (n // 2 - 1) * '수박'
        else:
            answer += (n // 2 - 1) * '수박' + '수'

    return answer

n_1 = 3
n_2 = 4

print(solution(n_1))
print(solution(n_2))

def solution_best(n):
    answer = '수박' * n

    return answer[:n]

print(solution_best(n_1))
print(solution_best(n_2))