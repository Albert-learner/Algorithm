# 29. 이상한 문자 만들기

def solution(s):
    answer = ''

    for word in s.split(' '):
        for i, c in enumerate(word):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
    return answer

s_1 = 'try hello world'

print(solution(s_1))

def solution_best(s):
    answer = ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower()
                                for i, c in enumerate(w)])
                       for w in s.split(' ')])

    return answer

print(solution_best(s_1))