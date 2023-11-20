# Restart 45. 콜라 문제

'''
Keypoint of this problem is thinking Mathmetically.
Catch the rule of Math formula.
'''
def solution(a, b, n):
    answer = 0

    rest_lst = [rest for rest in range(a)]
    while n not in rest_lst:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer

a_1 = 2
a_2 = 3

b_1 = 1
b_2 = 1

n_1 = 20
n_2 = 20

print(solution(a_1, b_1, n_1))
print(solution(a_2, b_2, n_2))