# 11. 같은 숫자는 싫어

# 완전 탐색 ... 잘못 생각함
def solution(arr):
    answer = []

    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer

arr_1 = [1, 1, 3, 3, 0, 1, 1]
arr_2 = [4, 4, 4, 3, 3]

print(solution(arr_1))
print(solution(arr_2))

def solution_best(arr):
    answer = arr[:1]

    for value in arr:
        if answer[-1] == value:
            continue
        answer.append(value)
    return answer

# print(solution_best(arr_1))
# print(solution_best(arr_2))

# pop을 하면 안 됨, 개수가 많아서
# def solution_error(arr):
#     answer = []
#
#     # 배열 맨 앞의 값
#     first = arr.pop(0)
#     answer.append(first)
#
#     for i in arr:
#         if i == first and i != answer[-1]:
#             answer.append(i)
#         elif i == first and i == answer[-1]:
#             continue
#         elif i != first and i not in answer:
#             answer.append(i)
#         elif i != first and i != answer[-1]:
#             answer.append(i)
#
#         first = arr.pop(0)
#
#     return answer

# print(solution_error(arr_1))
# print(solution_error(arr_2))



