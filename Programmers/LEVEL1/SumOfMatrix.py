# 27. 행렬의 덧셈
import numpy as np

def solution(arr1, arr2):
    answer = []

    tmp = []
    for a, b in zip(arr1, arr2):
        for c, d in zip(a, b):
           tmp.append(c + d)
        answer.append(tmp)
        tmp = []
    return answer

arr1_1 = [[1, 2], [2, 3]]
arr1_2 = [[1], [2]]

arr2_1 = [[3, 4], [5, 6]]
arr2_2 = [[3], [4]]

print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))
print()

def solution_other(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

    return answer

# print(solution_other(arr1_1, arr1_2))
# print(solution_other(arr2_1, arr2_2))
# print()

# 내 풀이
def solution_best(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)

    answer = A + B
    return answer

# print(solution_best(arr1_1, arr1_2))
# print(solution_best(arr2_1, arr2_2))