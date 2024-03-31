# 1010. 다리 놓기

"""
I didn't solve this problem by myself. I need to find the rule of math at problem.
This is about DP(Dynamic Programming), but finding math rule is easier to solve it.
See it again.
"""
# 1. My Solution(practice)
import math
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    bridges = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(bridges)

# # 1. My Solution
# import math
#
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     bridges = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
#     print(bridges)


# 2. Not my Solution
def factorial(N):
    num = 1
    for i in range(1, N + 1):
        num *= i

    return num

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    bridges = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridges)

"""
3
2 2
1 5
13 29
=>
1
5
67863915
"""