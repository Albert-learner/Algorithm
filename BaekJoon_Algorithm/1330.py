# 1330. 두 수 비교하기

A, B = map(int, input().split())

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")

"""
1 2
=>
<
========
10 2
=>
>
========
5 5
=>
==
"""