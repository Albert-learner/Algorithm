# 15. 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        else:
            continue

    if not answer:
        answer.append(-1)

    answer.sort()
    return answer

arr_1 = [5, 9, 7, 10]
arr_2 = [2, 36, 1, 3]
arr_3 = [3, 2, 6]

divisor_1 = 5
divisor_2 = 1
divisor_3 = 10

print(solution(arr_1, divisor_1))
print(solution(arr_2, divisor_2))
print(solution(arr_3, divisor_3))

def solution_best(arr, divisor):
    answer = sorted([n for n in arr if n % divisor == 0]) or [-1]

    return answer

# print(solution_best(arr_1, divisor_1))
# print(solution_best(arr_2, divisor_2))
# print(solution_best(arr_3, divisor_3))