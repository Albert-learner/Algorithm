# 57. 최솟값 만들기


def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse = True)

    sum_lst = []
    for a, b in zip(A, B):
        multiply = a * b
        sum_lst.append(multiply)

    answer = sum(sum_lst)
    return answer

A_1 = [1, 4, 2]
A_2 = [1, 2]

B_1 = [5, 4, 4]
B_2 = [3, 4]

print(solution(A_1, B_1))
print(solution(A_2, B_2))

def solution_best(A, B):
    answer = sum(a * b for a, b in zip(sorted(A), sorted(B, reverse = True)))

    return answer

print(solution_best(A_1, B_1))
print(solution_best(A_2, B_2))