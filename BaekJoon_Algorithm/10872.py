# 10872. 팩토리얼

N = int(input())

N_facto = 1
for i in range(1, N + 1):
    N_facto *= i

print(N_facto)

"""
10
=>
3728800
==========
0
=>
1
"""