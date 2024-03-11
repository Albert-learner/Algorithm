# 1312. 소수

# 1. My Solution
A, B, N = map(int, input().split())
answer = 0

for idx in range(N):
    A = (A % B) * 10
    answer = A // B

print(answer)


# # 2. Not my Solution
# A, B, N = map(int, input().split())
#
# for i in range(N):
#     A = (A % B) * 10
#     result = A // B
#
# print(result)

"""
3 4 1
=>
7
===========
25 7 5
=>
2
"""