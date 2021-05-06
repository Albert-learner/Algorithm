# 31. 문자열을 정수로 바꾸기

def solution(s):
    answer = ''

    answer += s
    answer = int(answer)
    return answer

str_1 = '1234'
str_2 = '-1234'

print(solution(str_1))
print(solution(str_2))