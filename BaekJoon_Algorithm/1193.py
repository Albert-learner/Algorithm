# 1193. 분수찾기

"""
I didn't solve this problem by myself. The key of this problem is finding rules for making fraction.
ZigZag sequence and I need to catch finding rules.
See it again.
"""
# 1. My Solution(practice)
N = int(input())

N_line = 1
while N > N_line:
    N -= N_line
    N_line += 1

if N_line % 2 == 0:
    numerator = N
    denominator = N_line - N + 1
else:
    numerator = N_line - N + 1
    denominator = N

print(f"{numerator}/{denominator}")

# 1193. 분수찾기

# 1. My Solution
N = int(input())

N_line = 1
while N > N_line:
    N -= N_line
    N_line += 1

if N_line % 2 == 0:
    numerator = N
    denominator = N_line - N + 1
else:
    numerator = N_line - N + 1
    denominator = N

print(f"{numerator}/{denominator}")


# 2. Not my Solution
num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')

"""
1
=>
1/1
=========
2
=>
1/2
=========
3
=>
2/1
=========
4
=>
3/1
=========
5
=>
2/2
=========
6
=>
1/3
=========
7
=>
1/4
=========
8
=>
2/3
=========
9
=>
3/2
=========
14
=>
2/4
"""