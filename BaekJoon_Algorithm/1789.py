# 1789. 수들의 합

"""
I didn't solve this problem by myself. I catch that this is related with Sum of Arithmetic Sequences.
But the key point is making S with many numbers as possible.
See it again.
"""
# 1. My Solution(Blog)
s = int(input())
total, count = 0, 0

while True:
    count += 1
    total += count
    if total > s:
        count -= 1
        break

print(count)

# 2. Not my Solution(Blog)
S = int(input())
i, cnt = 0, 0

while True:
    if S > i:
        i += 1
        S -= i
        cnt += 1
    else:
        print(cnt)
        break

print(cnt)
"""
200
=>
19
"""