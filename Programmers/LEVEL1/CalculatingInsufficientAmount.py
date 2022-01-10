# 52. 부족한 금액 계산하기

def solution(price, money, count):
    answer = sum([cnt * price for cnt in range(1, count + 1)]) - money

    if money > sum([cnt * price for cnt in range(1, count + 1)]):
        answer = 0

    return answer

price_1 = 3

money_1 = 20

count_1 = 4

print(solution(price_1, money_1, count_1))

def solution_best(price, money, count):
    answer = max(0, price * (count + 1) * count // 2 - money)

    return answer

print(solution_best(price_1, money_1, count_1))