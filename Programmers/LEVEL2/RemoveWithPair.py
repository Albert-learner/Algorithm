# 33. 짝지어 제거하기

# 자료구조 stack을 사용해야한다는 것까지는 갔으나...
def solution(s):
    answer = 0

    stack = []
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer

s_1 = 'baabaa'
s_2 = 'cdcd'

print(solution(s_1))
print(solution(s_2))