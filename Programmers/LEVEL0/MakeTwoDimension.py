# Restart 3. 2차원으로 만들기

# My Solution
def solution(num_list, n):
    answer = [num_list[num_idx:num_idx + n] for num_idx in range(0, len(num_list), n)]

    return answer

num_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
num_list_2 = [100, 95, 2, 4, 5, 6, 18, 33, 948]

n_1 = 2
n_2 = 3

print(solution(num_list_1, n_1))
print(solution(num_list_2, n_2))

import numpy as np
def solution_other(num_list, n):
    answer = 0

    arr = np.array(num_list).reshape(-1, n)
    answer = arr.tolist()
    return answer

print(solution_other(num_list_1, n_1))
print(solution_other(num_list_2, n_2))