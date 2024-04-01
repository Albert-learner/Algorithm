# 1309. 동물원

"""
I didn't solve this problem by myself. The key of this problem is finding math rules.
Find math rules elaborated(dp[i] = 2 * dp[i - 1] + dp[i - 2]).
See it again.
"""
# 1. My Solution(practice)
N = int(input())

if N == 1:
    print(3)
else:
    dp = [1 for _ in range(N + 1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    print(dp[N])

# 1. My Solution
N = int(input())

if N == 1:
    print(3)
else:
    dp = [1 for _ in range(N + 1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    print(dp[N])

# 2. Not my Solution
from sys import stdin
N = int(stdin.readline())

if N == 1:
    print(3)
else:
    dp = [1 for _ in range(N + 1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901
    print(dp[N])
"""
4
=>
41
"""