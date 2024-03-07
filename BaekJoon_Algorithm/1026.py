# 1026. 보물

# 1. My Solution
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_sort, B_rev_sort = sorted(A), sorted(B, reverse=True)
answer = 0
for a_element, b_element in zip(A_sort, B_rev_sort):
    answer += a_element * b_element

print(answer)

# 2. Not my Solution



"""
5
1 1 1 6 0
2 7 8 3 1
=>
18
===============
3
1 1 3
10 30 20
=>
80
===============
9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
=>
528
"""