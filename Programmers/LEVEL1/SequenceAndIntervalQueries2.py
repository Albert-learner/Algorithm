# Restart 32. 수열과 구간 쿼리 2

'''
I have to think about the initialization of possible list(poss_lst).
See again
'''
def solution(arr, queries):
    answer = []

    # for s, e, k in queries:
    #     sub_arr = arr[s:e + 1]
    #     poss_lst = [num for num in sub_arr if num > k]
    #
    #     try:
    #         answer.append(min(poss_lst))
    #     except:
    #         answer.append(-1)

    for s, e, k in queries:
        poss_lst = [num for num in arr[s:e + 1] if num > k]
        answer.append(-1 if len(poss_lst) == 0 else min(poss_lst))
    return answer

arr_1 = [0, 1, 2, 4, 3]

queries_1 = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

# print(solution(arr_1, queries_1))

def solution_best(arr, queries):
    answer = list(map(lambda x: -1 if x == 10 ** 6 else x,
                      [min(list(filter(lambda x : x > k, arr[s:e + 1])) +
                           [10 ** 6]) for s, e, k in queries]))

    return answer

print(solution_best(arr_1, queries_1))