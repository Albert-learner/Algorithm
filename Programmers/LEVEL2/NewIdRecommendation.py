# 19. 신규 아이디 추천

def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]

    return answer

new_id_1 = '...!@BaT#*..y.abcdefghijklm'
new_id_2 = 'z-+.^.'
new_id_3 = '=.='
new_id_4 = '123_.def'
new_id_5 = 'abcdefghijklmn.p'

# print(solution(new_id_1))
# print(solution(new_id_2))
# print(solution(new_id_3))
# print(solution(new_id_4))
# print(solution(new_id_5))

import re

def solution_best(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st


print(solution_best(new_id_1))
print(solution_best(new_id_2))
print(solution_best(new_id_3))
print(solution_best(new_id_4))
print(solution_best(new_id_5))