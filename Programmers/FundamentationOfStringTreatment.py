# 14. 문자열 다루기 기본

def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isdigit():
                answer = True
            else:
                answer = False
                break
    else:
        answer = False

    return answer

s_1 = 'a234'
s_2 = '1234'

# print(solution(s_1))
# print(solution(s_2))

def solution_best(s):
    answer = s.isdigit() and len(s) in (4, 6)

    return answer

# print(solution_best(s_1))
# print(solution_best(s_2))

import re

def solution_re(s):
    answer = bool(re.match('^(\d{4}|\d{6}$)', s))

    return answer

# print(solution_re(s_1))
# print(solution_re(s_2))