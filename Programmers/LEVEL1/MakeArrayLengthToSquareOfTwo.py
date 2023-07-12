# Restart 30. 배열의 길이를 2의 거븓제곱으로 만들기

def solution(arr):
    answer = arr

    zero_cnts = 0
    while len(answer) != 2 ** zero_cnts:
        if len(answer) == 2 ** zero_cnts:
            break

        if len(answer) > 2 ** zero_cnts:
            zero_cnts += 1
        else:
            chan = (2 ** zero_cnts) - len(answer)
            for _ in range(chan):
                answer.append(0)

    return answer

arr_1 = [1, 2, 3, 4, 5, 6]
arr_2 = [58, 172, 746, 89]

print(solution(arr_1))
print(solution(arr_2))

def solution_best(arr):
    zero_cnts = 1
    arr_len = len(arr)
    while zero_cnts < arr_len:
        zero_cnts *= 2

    answer = arr + [0] * (zero_cnts - arr_len)
    return answer

print(solution_best(arr_1))
print(solution_best(arr_2))