# 22. 정수 내림차순으로 배치하기

def solution(n):
    answer = 0

    # ['1', '1', '8', '3', '7', '2'] -> [8, 7, 3, 2, 1, 1]
    descend_lst = []

    # [8, 7, 3, 2, 1, 1] -> '873211'
    answer_str = ''

    for i in str(n):
        descend_lst.append(int(i))

    descend_lst.sort(reverse = True)
    for i in descend_lst:
        answer_str += str(i)

    answer = int(answer_str)
    return answer

n_1 = 118372

print(solution(n_1))

def solution_best(n):
    answer = int(''.join(sorted(list(str(n)), reverse = True)))

    return answer

print(solution_best(n_1))

def solution_other(n):
    answer = 0

    ls = list(str(n))
    ls.sort(reverse=True)
    answer = int(''.join(ls))
    return answer

print(solution_other(n_1))