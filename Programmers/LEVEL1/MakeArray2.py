# Restart 33. 배열 만들기 2

def solution(l, r):
    answer = []

    for int_num in range(l, r + 1):
        if all(num in ['0', '5'] for num in str(int_num)):
            answer.append(int_num)

    if len(answer) == 0:
        answer.append(-1)
    return answer

l_1 = 5
l_2 = 10

r_1 = 555
r_2 = 20

print(solution(l_1, r_1))
print(solution(l_2, r_2))

def solution_best(l, r):
    answer = []

    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)

    return answer if answer else [-1]

print(solution_best(l_1, r_1))
print(solution_best(l_2, r_2))