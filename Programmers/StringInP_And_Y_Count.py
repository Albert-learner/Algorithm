# 8. 문자열 내 p와 y의 개수

def solution(s):
    answer = True

    # p와 y 세는 변수 선언
    p_cnt = 0
    y_cnt = 0

    # 반복문 돌면서 개수 세기
    for i in s:
        if i == 'p' or i == 'p'.upper():
            p_cnt += 1
        elif i == 'y' or i == 'y'.upper():
            y_cnt += 1
        else:
            continue

    if p_cnt == y_cnt:
        answer = True
    else:
        answer = False

    return answer

s_1 = 'pPoooyY'
s_2 = 'Pyy'

print(solution(s_1))
print(solution(s_2))

def solution_best(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution_best(s_1))
print(solution_best(s_2))