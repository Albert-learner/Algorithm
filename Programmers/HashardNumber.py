# 26. 햐샤드 수

def solution(x):
    answer = True

    x_lst = [int(i) for i in str(x)]

    if x % sum(x_lst) == 0:
        answer = True
    else:
        answer = False
    return answer

x_1 = 10
x_2 = 12
x_3 = 11
x_4 = 13

print(solution(x_1))
print(solution(x_2))
print(solution(x_3))
print(solution(x_4))

def solution_best(x):
    answer = x % sum([int(c) for c in str(x)]) == 0

    return answer

# print(solution_best(x_1))
# print(solution_best(x_2))
# print(solution_best(x_3))
# print(solution_best(x_4))