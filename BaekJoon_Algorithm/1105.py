# 1105. 팔

"""
I almost solve this problem by myself. But I miss Memory Excess and Time Excess.
Not using sort function. Try to memorize this problem by Greedy problem.
See it again.
"""
# 1. My Solution(practice, greedy)
A, B = map(str, input().split())

min_eight_cnts = 0
if len(A) != len(B):
    print(0)
else:
    for chr_idx in range(len(A)):
        if A[chr_idx] == B[chr_idx]:
            if A[chr_idx] == '8':
                min_eight_cnts += 1
        else:
            break

    print(min_eight_cnts)


# 2. My Solution(practice, mine)
L, R = map(int, input().split())

min_eight_cnts = float("inf")

for num in range(L, R + 1):
    eight_cnts = str(num).count('8')
    min_eight_cnts = min(min_eight_cnts, eight_cnts)
    if min_eight_cnts == 0:
        break

print(min_eight_cnts)

####################################################################
# 1. My Solution
L, R = map(int, input().split())

min_cnt = float("inf")

for num in range(L, R + 1):
    cnt_eight = str(num).count('8')
    min_cnt = min(min_cnt, cnt_eight)
    if min_cnt == 0:
        break

print(min_cnt)


# 2. Not my Solution
A, B = map(str, input().split(' '))

ret = 0

if len(A) != len(B):
    print(0)
else:
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                ret += 1
        else:
            break
    print(ret)
"""
1 10
=>
0
=============
88 88
=>
2
=============
800 899
=>
1
=============
8808 8880
=>
2
"""