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

# print(solution(s_1))
# print(solution(s_2))

def solution_other(s):
    answer = []

    for ch in s:
        if not answer:
            answer.append(ch)
        else:
            if answer[-1] == ch:
                answer.pop()
            else:
                answer.append(ch)

    return int(not(answer))

print(solution_other(s_1))
print(solution_other(s_2))

def solution_best(s):
    answer = 0

    stack = []
    for ch in s:
        if stack[-1:] == [ch]:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        answer = 1
    return answer

print(solution_best(s_1))
print(solution_best(s_2))