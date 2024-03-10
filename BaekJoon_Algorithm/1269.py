# 1269. 대칭 차집합

# 1. My Solution
A_elements, B_elements = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))

# 2. Not my Solution



"""
3 5
1 2 4
2 3 4 5 6
=>
4
==============
"""