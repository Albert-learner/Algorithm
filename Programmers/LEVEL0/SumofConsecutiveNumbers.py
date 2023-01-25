# Restart 23. 연속된 수의 합

def solution(num, total):
    answer = []

    x = (total - sum(range(1, num))) // num
    answer = [x + i for i in range(num)]
    return answer

num_1 = 3
num_2 = 5
num_3 = 4
num_4 = 5

total_1 = 12
total_2 = 15
total_3 = 14
total_4 = 5

print(solution(num_1, total_1))
print(solution(num_2, total_2))
print(solution(num_3, total_3))
print(solution(num_4, total_4))

def solution_best(num, total):
    answer = [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

    return answer

print(solution_best(num_1, total_1))
print(solution_best(num_2, total_2))
print(solution_best(num_3, total_3))
print(solution_best(num_4, total_4))