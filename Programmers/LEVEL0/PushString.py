# Restart 13. 문자열 밀기

# My Solution
from collections import deque
def solution(A, B):
    answer = 0

    A_deq = deque(A)
    push_cases = []
    for idx in range(len(A)):
        last_char = A_deq.pop()
        A_deq.appendleft(last_char)
        push_cases.append(''.join(A_deq))

    if B in push_cases:
        answer = push_cases.index(B) + 1

    # 이 부분도 고려했어야 함!!!
    if A == B:
        answer = 0
    return answer

A_1 = 'hello'
A_2 = 'apple'

B_1 = 'ohell'
B_2 = 'elppa'

# print(solution(A_1, B_1))
# print(solution(A_2, B_2))

solution_best = lambda a, b:(b * 2).find(a)

print(solution_best(A_1, B_1))
print(solution_best(A_2, B_2))