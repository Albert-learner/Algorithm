# 1. 평균 구하기

def solution(arr):
    answer = sum(arr) / len(arr)

    return answer

arr_1 = [1, 2, 3, 4]
arr_2 = [5, 5]

print(solution(arr_1))
print(solution(arr_2))

# def solution_1(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     answer = sum / len(arr)
#     return answer