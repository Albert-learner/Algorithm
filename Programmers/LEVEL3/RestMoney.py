# 7. 거스름돈

def solution(n, money):
    answer = 0

    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]

    answer = dp[n] %  1000000007
    return answer

n_1 = 5

money_1 = [1, 2, 5]

print(solution(n_1, money_1))
