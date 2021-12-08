# 51. 나머지가 1이 되는 수 찾기

def solution(n):
    answer = 0

    res_lst = [n % i for i in range(1, n + 1)]
    for rest in res_lst:
        if rest == 1:
            answer = res_lst.index(rest) + 1
            break

    return answer

n_1 = 10
n_2 = 12

# print(solution(n_1))
# print(solution(n_2))

def solution_other(n):
    answer = 0

    for divisor in range(2, (n - 1 // 2) + 1):
        if (n - 1) % divisor == 0:
            answer = divisor
            break
        else:
            answer = n - 1

    return answer

# print(solution_other(n_1))
# print(solution_other(n_2))

def solution_best(n):
    answer = min([x for x in range(1, n + 1) if n % x == 1])

    return answer

# print(solution_best(n_1))
# print(solution_best(n_2))