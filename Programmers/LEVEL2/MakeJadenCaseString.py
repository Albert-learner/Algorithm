# 59. JadenCase 문자열 만들기

'''
공백문자가 반복되어 나올 수 있으며 반복 되어 나온 공백은 문자열로 취급하지 않습니다
라는 조건이 명시되어 있지 않아 틀렸던 문제, 거의 다 맞춤.
'''
def solution(s):
    answer = ' '.join([word.title() if word.isalpha()  else word.lower() for word in s.split(' ')])

    return answer

s_1 = "3people unFollowed me"
s_2 = "for the last week"

print(solution(s_1))
print(solution(s_2))

def solution_mine(s):
    answer = ' '.join([word.title() if word.isalpha()  else word
                       for word in s.split()])

    return answer

print(solution_mine(s_1))
print(solution_mine(s_2))

def solution_good(s):
    answer = ' '.join([word.capitalize() for word in s.split(' ')])

    return answer

print(solution_good(s_1))
print(solution_good(s_2))