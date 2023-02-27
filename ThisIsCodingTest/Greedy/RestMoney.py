# 3-1. 거스름돈

# N = int(input('Total Money : '))
#
# coins_type = [50, 10, 500, 100]
#
# counts = 0
# coins_type.sort(reverse = True)
# for coin in coins_type:
#     counts += N // coin
#     N %= coin
#
# print(counts)

# Programmers style

def solution(money):
    answer = 0

    coins_type = [10, 50, 100, 500]
    coins_type.sort(reverse = True)
    coin_cnts = 0
    for coin in coins_type:
        coin_cnts += money // coin
        money %= coin

    answer = coin_cnts
    return answer

money_1 = 1260
print(solution(money_1))