# 17. 가운데 문자 가져오기

def solution(s):
    length = len(s)
    answer = ''

    if length % 2 == 0:
        answer = s[length // 2 - 1:length // 2 + 1]
    else:
        answer = s[length // 2]
    return answer

s_1 = 'abcde'
s_2 = 'qwer'

print(solution(s_1))
print(solution(s_2))

def solution_best(s):
    answer = s[(len(s) - 1) // 2: len(s) // 2 + 1]

    return answer

print(solution_best(s_1))
print(solution_best(s_2))