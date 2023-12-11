# 1. 연속된 문자 A 제거

S = input()

# 1. Use deque for solving this problem
from collections import deque

change_str = ""
s_idx = 0
S_que = deque(map(str, S))
while len(S_que) != 1:
    if S_que[s_idx] in ['a', 'A'] and S_que[s_idx + 1] in ['a', 'A']:
        S_que.popleft()
        S_que.popleft()
        S_que.appendleft('a')
    else:
        front_chr = S_que.popleft()
        change_str += front_chr

change_str += S_que.pop()
print(change_str)

# 2. Use Python re module(recommend Solution)
import re

pattern = re.compile("[aA]{2,}")
result = pattern.findall(S)
print(re.sub(pattern, 'a', S))

# 3. Book Solution(Too much complicated, not recommend)
def solution(S):
    answer = ""
    i = 0

    while i < len(S):
        if S[i] != 'a' and S[i] != 'A':
            answer += S[i]
            i += 1
            continue

        j = i + 1
        while j < len(S):
            if S[j] != 'a' and S[j] != 'A':
                break
            j += 1

        if j - i == 1:
            answer += S[i]
        else:
            answer += S[i].lower()
        i = j

    return answer

print(solution(S))
"""
ZZaAAbBAAA
=> ZZabBa

ABAaaAAAaab
=> ABab
"""