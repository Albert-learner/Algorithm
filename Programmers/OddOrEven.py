# 33. 짝수와 홀수

def solution(num):
    answer = ''

    if num % 2 == 0:
        answer += 'Even'
    else:
        answer += 'Odd'
    return answer

num_1 = 3
num_2 = 4

print(solution(num_1))
print(solution(num_2))

def solution_best(num):
    answer = 'Even' if num % 2 == 0 else 'Odd'

    return answer

print(solution_best(num_1))
print(solution_best(num_2))