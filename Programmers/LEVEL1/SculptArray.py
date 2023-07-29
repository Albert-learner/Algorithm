# Restart 35. 배열 조각하기

'''
I solve it, but it didn't satisfy time efficiency.
See how to satisfy time complex.
'''
def solution(arr, query):
    answer = arr

    for q_idx in range(len(query)):
        if q_idx % 2 == 0:
            answer = answer[:query[q_idx] + 1]
        else:
            answer = answer[query[q_idx]:]
    return answer

arr_1 = [0, 1, 2, 3, 4, 5]

query_1 = [4, 1, 2]

print(solution(arr_1, query_1))

def solution_similar(arr, query):
    answer = arr

    for q_idx, q in enumerate(query):
        if q_idx % 2 == 0:
            answer = answer[:query[q_idx] + 1]
        else:
            answer = answer[query[q_idx]:]
    return answer

print(solution_similar(arr_1, query_1))

'''
This is my method.

'''
def solution_error(arr, query):
    answer = []

    for q_idx in range(len(query)):
        # print('arr :', arr)
        arr_q_idx = arr.index(query[q_idx])
        if q_idx != 0:
            if q_idx % 2 == 0:
                answer = answer[:arr_q_idx + 1]
            else:
                answer = answer[arr_q_idx:]
        else:
            answer = arr[:arr_q_idx + 1]
        # print('answer :', answer)
    return answer

# print(solution_error(arr_1, query_1))

