# 23. 제일 작은 수 제거하기

def solution(arr):
    answer = []

    if len(arr) == 1:
        answer = [-1]
    else:
        min_cost = min(arr)
        for i in arr:
            if i == min_cost:
                arr.remove(i)

        for i in arr:
            answer.append(i)
    return answer

arr_1 = [4, 3, 2, 1]
arr_2 = [10]

# print(solution(arr_1))
# print(solution(arr_2))

def solution_best(arr):
    answer = [i for i in arr if i > min(arr)]

    return answer

print(solution_best(arr_1))
print(solution_best(arr_2))