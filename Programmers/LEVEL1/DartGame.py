# 39. 다트 게임

# 내 풀이 X ... 뭔가 복잡해
def solution(dartResult):
    answer = 0

    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'*' : 2, '#' : -1}

    Third_period = [0, 0, 0]
    flag = -1

    for idx, dart in enumerate(dartResult):
        if dart.isdigit():
            flag += 1
            if dart == '0':
                continue
            elif dartResult[idx + 1].isdigit():  # 10 이상일 때
                Third_period[flag] = int(dart) * 10
                flag -= 1
            else:
                Third_period[flag] = int(dart)
        elif dart in 'SDT':  # SDT
            Third_period[flag] **= bonus[dart]
        else:
            if dart == '*':
                Third_period[flag - 1] *= 2

            Third_period[flag] *= option[dart]

    answer = sum(Third_period)
    return answer

dartResult_1 = '1S2D*3T'
dartResult_2 = '1D2S#10S'
dartResult_3 = '1D2S0T'
dartResult_4 = '1S*2T*3S'
dartResult_5 = '1D#2S*3S'
dartResult_6 = '1T2D3D#'
dartResult_7 = '1D2S3T*'

print(solution(dartResult_1))
print(solution(dartResult_2))
print(solution(dartResult_3))
print(solution(dartResult_4))
print(solution(dartResult_5))
print(solution(dartResult_6))
print(solution(dartResult_7))

import re

def solution_best(dartResult):
    answer = 0

    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution_best(dartResult_1))
print(solution_best(dartResult_2))
print(solution_best(dartResult_3))
print(solution_best(dartResult_4))
print(solution_best(dartResult_5))
print(solution_best(dartResult_6))
print(solution_best(dartResult_7))