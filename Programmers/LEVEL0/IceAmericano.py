# Restart 1. 아이스 아메리카노

def solution(money):
    answer = []

    americano = 5500
    answer += divmod(money, americano)

    return answer

money_1 = 5500
money_2 = 15000

print(solution(money_1))
print(solution(money_2))

def solution_other(money):
    answer = [money // 5500, money % 5500]

    return answer

print(solution_other(money_1))
print(solution_other(money_2))