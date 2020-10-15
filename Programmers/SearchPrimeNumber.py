# 4. 소수 찾기
import math

def solution(n):
    answer = 0
    prime = [True] * (n + 1)
    m = int(math.sqrt(n))

    for i in range(2, m + 1):
        if prime[i] == True:
            for j in range(i+i, n+1, i):
                prime[j] = False

    prime_total = [i for i in range(2, n+1) if prime[i] == True]
    answer = len(prime_total)
    return answer

n_1 = 10
n_2 = 5

# print(solution(n_1))
# print(solution(n_2))

def solution_best(n):
    answer = 0
    num = set(range(2, n + 1))
    # print(num)

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
            # print(num)

    answer = len(num)
    return answer

print(solution_best((n_1)))
print(solution_best(n_2))