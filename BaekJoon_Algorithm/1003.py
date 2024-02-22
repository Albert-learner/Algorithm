# 1003. 피보나치 함수

"""
I solve this problem by myself with Recursion, but I have to consider Time Complexity and Memory Complexity.
See it again for solving those problems with tricks.
"""

# 1. My Solution(Use DP, but got Memory exceeded)
import sys
input = sys.stdin.readline

# # # Recursion is easy, but it makes Time Exceeded
# # def Fibonacci(num):
# #     if num == 0:
# #         return "0"
# #     elif num == 1:
# #         return "1"
# #     else:
# #         return Fibonacci(num - 1) + Fibonacci(num - 2)

# 2. Use Dynamic Programming, but Memory Exceeded
def Fibonacci(num):
    if num < 0 or num > 40:
        return

    fib_sequence = ["0", "1"]
    for i in range(2, num + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[num]

# Same as previous method
# def Fibonacci(num):
#     if num < 0 or num > 40:
#         return
#
#     a, b = str("0"), str("1")
#     for _ in range(2, num + 1):
#         a, b = b, a + b
#
#     return str(b)

T = int(input())
cases = [int(input()) for _ in range(T)]
for case in cases:
    binary_str = Fibonacci(case)
    zero_cnts, one_cnts = binary_str.count("0"), binary_str.count("1")
    print(zero_cnts, one_cnts)

# 2. Not my solution
T = int(input())
for tc in range(T):
    N = int(input())
    zero_cnts = [1, 0]
    one_cnts = [0, 1]

    for i in range(2, N + 1):
        zero_cnts.append(zero_cnts[i - 1] + zero_cnts[i - 2])
        one_cnts.append(one_cnts[i - 1] + one_cnts[i - 2])

    print("{} {}".format(zero_cnts[N], one_cnts[N]))

"""
3
0
1
3
=>
1 0
0 1
1 2
==========
2
6
22
=>
5 8
10946 17711
===========
2
40
0
=>
63245986 102334155
1 0
"""