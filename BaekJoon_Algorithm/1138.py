# 1138. 한 줄로 서기

"""
This requires Ability to understand text.
I didn't catch what requires in this problem.
"""
# 1. My Solution
N = int(input())
memory = list(map(int, input().split()))

answer = [0] * N
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == memory[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)

# # 2. Not my Solution
# n = int(input())
#
# arr = list(map(int, input().split()))
# answer = [0] * n
#
# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if cnt == arr[i] and answer[j] == 0:
#             answer[j] = i + 1
#             break
#         elif answer[j] == 0:
#             cnt += 1
#
# print(' '.join(map(str, answer)))

"""
4
2 1 1 0
=>
4 2 1 3
==========
5
0 0 0 0 0
=>
1 2 3 4 5
==========
6
5 4 3 2 1 0
=>
6 5 4 3 2 1
=============
7
6 1 1 1 2 0 0
=>
6 2 3 4 7 5 1
"""