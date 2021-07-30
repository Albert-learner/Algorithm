# 61. 괄호 변환

def balanced(p):
    num = 0
    tmp = []

    for idx, value in enumerate(p):
        if value == '(':
            num += 1
        elif value == ')':
            num -= 1

        if num == 0:
            return idx

def correct(string):
    tmp = []

    for i in string:
        if i == '(':
            tmp.append(i)
        else:
            if len(tmp) == 0:
                return False
            tmp.pop()

    if len(tmp) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''

    if p == '' or correct(p):
        return p

    u, v = p[:balanced(p) + 1], p[balanced(p) + 1:]
    if correct(u):
        string = solution(v)
        return u + string
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('

        answer += ''.join(u)

    return answer

p_1 = "(()())()"
p_2 = ")("
p_3 = "()))((()"

# print(solution(p_1))
# print(solution(p_2))
# print(solution(p_3))

'''
비슷한 풀이, 좀 더 좋은 풀이
'''
from collections import Counter
def is_balanced(p):
    bracket_counter = Counter(p)
    bal = bracket_counter['('] - bracket_counter[')']

    return not(bool(bal))

def is_right(p):
    if is_balanced(p) == False:
        return False

    bracket_counter = Counter(p)
    bal = bracket_counter['('] - bracket_counter[')']
    if bal < 0:
        return False

    return True

def solution_other(p):
    answer = ''

    if is_right(p) == True:
        return p

    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[:i]) == True:
            u, v = p[:i], p[i:]
            break

    if is_right(u) == True:
        return u + solution_other(v)
    else:
        answer = '(' + solution_other(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                if i == '(':
                    answer += ')'
                else:
                    answer += '('

        return answer

# print(solution_other(p_1))
# print(solution_other(p_2))
# print(solution_other(p_3))

def solution_best(p):
    if p == '': return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(': c -= 1
        else: c += 1
        if c > 0: r = False
        if c == 0:
            if r:
                return p[:i + 1] + solution_best(p[i + 1:])
            else:
                return '(' + solution_best(p[i + 1:]) + ')' + ''.join(list(
                                map(lambda x:'(' if x==')' else ')',p[1:i])))

# print(solution_best(p_1))
# print(solution_best(p_2))
# print(solution_best(p_3))