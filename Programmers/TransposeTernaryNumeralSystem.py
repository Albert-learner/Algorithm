# 41. 삼진법 뒤집기

# 어디가 틀린거지??? 내 풀이 ㅠㅠ
def solution(n):
    answer = 0

    Ternary_str = ''
    while n > 0:
        Ternary_str += str(n % 3)
        n //= 3

    cnt = 1
    for each_chr in reversed(Ternary_str):
        answer += cnt * int(each_chr)
        cnt *= 3

    return answer

n_1 = 45
n_2 = 125

print(solution(n_1))
print(solution(n_2))

def solution_error(n):
    answer = 0

    # 3진법 문자열 -> '1200'
    Ternary_str = ''

    quota, rest = n // 3, n % 3
    Ternary_str += str(rest)

    if n != 1:
        # 45 -> '1200' -> '0021'
        while quota > 3:
            rest = quota % 3
            quota //= 3
            Ternary_str += str(rest)
        Ternary_str += str(quota)

    # 10진법 리스트 ... '0021' -> [0, 0, 2, 1]
    Decimal_lst = [int(i) for i in Ternary_str]

    for i in range(len(Decimal_lst)):
        answer += Decimal_lst[i] * (3 ** (len(Decimal_lst) - i - 1))
    return answer

# print(solution_error(n_1))
# print(solution_error(n_2))