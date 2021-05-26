# 39. 다트 게임

# 내 풀이 X ... 뭔가 복잡해
def solution(dartResult):
    answer = 0

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}

    chances = [0, 0, 0]
    number_cnt = -1
    for idx, dart in enumerate(dartResult):
        if dart.isdigit():
            number_cnt += 1
            if dart == '0':
                continue
            # 10일 때
            elif dartResult[idx + 1].isdigit():
                chances[number_cnt] = int(dart) * 10
                number_cnt -= 1
            else:
                chances[number_cnt] = int(dart)
        elif dart in 'SDT':
            chances[number_cnt] **= bonus[dart]
        else:
            if dart == '*':
                chances[number_cnt - 1] *= 2
            else:
                chances[number_cnt - 1] *= -1

    answer = sum(chances)
    return answer

dartResult_1 = '1S2D*3T'
dartResult_2 = '1D2S#10S'
dartResult_3 = '1D2S0T'
dartResult_4 = '1S*2T*3S'
dartResult_5 = '1D#2S*3S'
dartResult_6 = '1T2D3D#'
dartResult_7 = '1D2S3T*'

# print(solution(dartResult_1))
# print(solution(dartResult_2))
# print(solution(dartResult_3))
# print(solution(dartResult_4))
# print(solution(dartResult_5))
# print(solution(dartResult_6))
# print(solution(dartResult_7))

def solution_other(dartResult):
    answer = []

    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1

    return sum(answer)

# print(solution_other(dartResult_1))
# print(solution_other(dartResult_2))
# print(solution_other(dartResult_3))
# print(solution_other(dartResult_4))
# print(solution_other(dartResult_5))
# print(solution_other(dartResult_6))
# print(solution_other(dartResult_7))

import re

def solution_best(dartResult):
    answer = 0

    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# print(solution_best(dartResult_1))
# print(solution_best(dartResult_2))
# print(solution_best(dartResult_3))
# print(solution_best(dartResult_4))
# print(solution_best(dartResult_5))
# print(solution_best(dartResult_6))
# print(solution_best(dartResult_7))

