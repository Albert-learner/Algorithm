# 1149. RGB 거리

# 1. My Solution
N = int(input())
possible_colors = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = possible_colors[0]

for r_idx in range(1, N):
    for c_idx in range(3):
        dp[r_idx][c_idx] = possible_colors[r_idx][c_idx] + min(dp[r_idx - 1][(c_idx + 1) % 3],
                                                               dp[r_idx - 1][(c_idx + 2) % 3])

print(min(dp[N - 1]))

# # 2. Not my Solution(chatGPT)
# N = int(input())
# possible_colors = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [[0] * 3 for _ in range(N)]
# dp[0] = possible_colors[0]
#
# for i in range(1, N):
#     for j in range(3):
#         dp[i][j] = possible_colors[i][j] + min(dp[i - 1][(j + 1) % 3],
#                                                dp[i - 1][(j + 2) % 3])
#
# print(min(dp[N - 1]))

# 3. Not my Solution(Blog)
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(1, n):  # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0] = min(a[i - 1][1], a[i - 1][2]) + a[i][0]
    a[i][1] = min(a[i - 1][0], a[i - 1][2]) + a[i][1]
    a[i][2] = min(a[i - 1][0], a[i - 1][1]) + a[i][2]

print(min(a[n - 1][0], a[n - 1][1], a[n - 1][2]))
"""
3
26 40 83
49 60 57
13 89 99
=>
96
==============
3
1 100 100
100 1 100
100 100 1
=>
3
==============
3
1 100 100
100 100 100
1 100 100
=>
102
==============
6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91
=>
208
==============
8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19
=>
253
"""