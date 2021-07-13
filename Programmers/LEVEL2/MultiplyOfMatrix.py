# 52. 행렬의 곱셈

def solution(arr1, arr2):
    answer = [[]]

    answer = [[sum(r * c for r, c in zip(row, col))
               for col in zip(*arr2)] for row in arr1]
    return answer

arr1_1 = [[1, 4], [3, 2], [4, 1]]
arr1_2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]

arr2_1 = [[3, 3], [3, 3]]
arr2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1_1, arr2_1))
print(solution(arr1_2, arr2_2))

import numpy as np

def solution_best(arr1, arr2):
    answer = [[]]

    ar1 = np.array(arr1)
    ar2 = np.array(arr2)
    answer = np.dot(ar1, ar2).tolist()
    return answer

# print(solution_best(arr1_1, arr2_1))
# print(solution_best(arr1_2, arr2_2))