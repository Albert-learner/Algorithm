# 26307. Correct

# 1. My Solution
HH, MM = map(int, input().split())
start_time = 540
end_time = HH * 60 + MM
print(end_time - start_time)

"""
9 0
=>
0
============
11 59
=>
179
"""