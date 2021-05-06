# 21. 자릿수 더하기

def solution(n):
    answer = 0

    # 123 -> '123'
    str_n = str(n)

    # '123' -> [1, 2, 3]
    n_lst = []

    for i in str_n:
        n_lst.append(int(i))

    answer = sum(n_lst)
    return answer

n_1 = 123
n_2 = 987

print(solution(n_1))
print(solution(n_2))

def solution_best(n):
    answer = sum([int(i) for i in str(n)])

    return answer

print(solution_best(n_1))
print(solution_best(n_2))