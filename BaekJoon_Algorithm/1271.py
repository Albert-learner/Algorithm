# 1271. 엄청난 부자 2

# 1. My Solution
n, m = map(int, input().split())

div_money, rest = divmod(n, m)
print(div_money, rest)
# 2. Not my Solution


"""
1000 100
=>
10
0
===========
"""