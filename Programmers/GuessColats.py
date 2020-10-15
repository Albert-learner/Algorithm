# 25. 콜라츠 추측

def solution(num):
    answer = 0

    while num != 1:
        if answer < 500:
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            answer += 1
        else:
            answer = -1
            return answer
    return answer

num_1 = 6
num_2 = 16
num_3 = 626331

print(solution(num_1))
print(solution(num_2))
print(solution(num_3))

def solution_best(num):
    answer = -1

    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1

        if num == 1:
            answer = num + 1
            return answer
    return answer

print(solution_best(num_1))
print(solution_best(num_2))
print(solution_best(num_3))