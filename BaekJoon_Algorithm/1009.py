# 1009. 분산처리

"""
I catch this problem is based on rules of end number at decimal numbers.
But I miss multiply number of 10.
"""
# 1. My Solution
test_cases = int(input())
for case in range(test_cases):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        b %= 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b %= 4
        if b == 0:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)

# 2. Not my Solution
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)

"""
5
1 6
3 7
6 2
7 100
9 635
=>
1
7
6
1
9
==========
3
19 34
20 10
50 100
=>
9
0
0
"""