# Restart 20. 최빈값 구하기
'''
My Solution : use Counter object to find most common values
'''
from collections import Counter
def solution(array):
    answer = 0

    arr_counter = Counter(array)
    arr_cntr_sort = arr_counter.most_common()
    count_lst = [arr_cntr[1] for arr_cntr in arr_cntr_sort]
    if count_lst[0] in count_lst[1:]:
        answer = -1
    else:
        answer = arr_cntr_sort[0][0]

    return answer

array_1 = [1, 2, 3, 3, 3, 4]
array_2 = [1, 1, 2, 2]
array_3 = [1]

print(solution(array_1))
print(solution(array_2))
print(solution(array_3))

'''
Not using Counter object, but see this method.
'''
def solution_best(array):
    answer = -1

    while len(array) != 0:
        for idx, value in enumerate(set(array)):
            array.remove(value)
        if idx == 0: return value
    return answer

print(solution_best(array_1))
print(solution_best(array_2))
print(solution_best(array_3))