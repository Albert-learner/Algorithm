# 31. k진수에서 소수 개수 구하기

def change_k_num(n, k):
    change = ''

    while n > 0:
        n, mod = divmod(n, k)
        change += str(mod)

    return change[::-1]

def solution(n, k):
    answer = 0

    change_k = change_k_num(n, k)
    change_k = change_k.split('0')

    for num in change_k:
        if len(num) == 0:
            continue
        if int(num) < 2:
            continue

        # 에라토스테네스의 체
        prime_number = True
        for i in range(2, int(int(num) ** 0.5) + 1):
            if int(num) % i == 0:
                prime_number = False
                break

        if prime_number:
            answer += 1

    return answer

n_1 = 437674
n_2 = 110011

k_1 = 3
k_2 = 10

print(solution(n_1, k_1))
print(solution(n_2, k_2))

def solution_other(n, k):
    answer = 0

    change_k = ''
    while n:
        change_k = str(n % k) + change_k
        n //= k

    change_k = change_k.split('0')

    for num in change_k:
        if len(num) == 0:
            continue
        if int(num) < 2:
            continue

        prime_number = True
        for i in range(2, int(int(num) ** 0.5) + 1):
            if int(num) % i == 0:
                prime_number = False
                break

        if prime_number:
            answer += 1

    return answer

n_1 = 437674
n_2 = 110011

k_1 = 3
k_2 = 10

print(solution_other(n_1, k_1))
print(solution_other(n_2, k_2))