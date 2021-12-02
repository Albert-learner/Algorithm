# 49. 없는 숫자 더하기

def solution(numbers):
    answer = 0

    all_num = [i for i in range(10)]
    for number in all_num:
        if number not in numbers:
            answer += number

    return answer

numbers_1 = [1, 2, 3, 4, 6, 7, 8, 0]
numbers_2 = [5, 8, 4, 0, 6, 7, 9]

print(solution(numbers_1))
print(solution(numbers_2))

def solution_best(numbers):
    answer = 45 - sum(numbers)

    return answer

print(solution_best(numbers_1))
print(solution_best(numbers_2))