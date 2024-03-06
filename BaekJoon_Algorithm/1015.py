# 1015. 수열 정렬

"""
I didn't solve this problem by myself. I didn't catch '비내림수' in this problem.
Think simple and catch the main point quickly.
"""
# 1. My Solution
P_size = int(input())
A_sequence = list(map(int, input().split()))

A_sort = sorted(A_sequence)
B_sequence = []
for i in range(P_size):
    B_sequence.append(A_sort.index(A_sequence[i]))
    A_sort[A_sort.index(A_sequence[i])] = -1

for i in range(P_size):
    print(str(B_sequence[i]), end=' ')

# 2. Not my Solution
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sortA = sorted(A, reverse=False)

P = []
for i in range(N):
    P.append(sortA.index(A[i]))
    sortA[sortA.index(A[i])] = -1

for i in range(N):
    print(str(P[i]), end=' ')


"""
3
2 3 1
=>
1 2 0
=========
4
2 1 3 1
=>
2 0 3 1
=========
8
4 1 6 1 3 6 1 4
=>
4 0 6 1 3 7 2 5
"""