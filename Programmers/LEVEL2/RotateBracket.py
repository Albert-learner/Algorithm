# 40. 괄호 회전하기

# 쉽게 생각하기(stack으로 구현해서 푼다는 idea
def solution(s):
    answer = 0

    dic = {'(' : ')', '{' : '}', '[' : ']'}
    for i in range(len(s)):
        rotate_s = list(s[i:] + s[:i])
        stack = []
        # 여기 부분을 구현 못함.
        while rotate_s:
            ch = rotate_s.pop(0)
            if not stack:
                stack.append(ch)
            else:
                if stack[-1] in [')', '}', ']']:
                    break

                if dic[stack[-1]] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
        if not stack:
            answer += 1

    return answer

s_1 = '[](){}'
s_2 = '}]()[{'
s_3 = '[)(]'
s_4 = '}}}'

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))
print(solution(s_4))

'''
stack으로 푼다는 것 인지하고 얼추 구현했으나 마지막 부분을 못함.
괄호 개수로 먼저 비교한 후 회전하였을 때 비교하려고 했으나 
개수를 생각할 필요 없이 회전만 고려하면 해결되었던 문제...
'''
from collections import Counter
def solution_mine(s):
    answer = 0

    # 사실 필요없던 부분(갯수 세는 부분)
    bracket_counter = Counter(s)
    left_cnts, right_cnts = 0, 0
    for key, value in bracket_counter.items():
        if key in ['(', '{', '[']:
            left_cnts += value
        else:
            right_cnts += value

    if left_cnts != right_cnts:
        answer = 0
        return answer

    dic = {'(' : ')', '{' : '}', '[' : ']'}
    for i in range(len(s)):
        rotate_s = list(s[i:] + s[:i])
        stack = []
        while rotate_s:
            ch = rotate_s.pop(0)
            if not stack:
                stack.append(ch)
            else:
                if stack[-1] in [')', '}', ']']:
                    break

                if dic[stack[-1]] == ch:
                    stack.pop()
                else:
                    stack.append(ch)

        if not stack:
            answer += 1

    return answer

print(solution_mine(s_1))
print(solution_mine(s_2))
print(solution_mine(s_3))
print(solution_mine(s_4))

# 다른 풀이
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution_other(s):
    answer = 0

    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])

    return answer

print(solution_other(s_1))
print(solution_other(s_2))
print(solution_other(s_3))
print(solution_other(s_4))