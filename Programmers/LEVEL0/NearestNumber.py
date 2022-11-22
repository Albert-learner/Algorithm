# Restart 5. 가장 가까운 수

# My Solution
'''
이렇게 풀면 [8, 6], 7과 같이 순서가 바뀐 경우에는 해결되지 않음
'''
def solution(array, n):
    answer = 0

    dif_arr = [arr - n if arr > n else n - arr for arr in array]
    min_arr_idx = dif_arr.index(min(dif_arr))
    answer = array[min_arr_idx]

    return answer

array_1 = [3, 10, 28]
array_2 = [10, 11, 12]

n_1 = 20
n_2 = 13

# print(solution(array_1, n_1))
# print(solution(array_2, n_2))

# Unique Solution
solution_unique = lambda a, n:sorted(a, key = lambda x : (abs(x - n), x))[0]

# print(solution_unique(array_1, n_1))
# print(solution_unique(array_2, n_2))

# Other Solution
def solution_other(array, n):
    answer = 0

    array.sort(key = lambda x : (abs(x - n), x - n))
    answer = array[0]
    return answer

# print(solution_other(array_1, n_1))
# print(solution_other(array_2, n_2))

# Best Solution
def solution_best(array, n):
    # print(sorted([index, abs(n - num), num] for index, num in enumerate(array)))
    # print(sorted([[index, abs(n - num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1])))
    # print(sorted([[index, abs(n - num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0])
    # print(sorted([[index, abs(n - num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0])
    answer = array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]

    return answer

# print(solution_best(array_1, n_1))
# print(solution_best(array_2, n_2))