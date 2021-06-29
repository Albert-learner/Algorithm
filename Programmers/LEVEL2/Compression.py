# 47. 압축

def solution(msg):
    answer = []

    dict = {chr(65 + i) : i + 1 for i in range(26)}
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dict[msg[w:c]])
            break

        if msg[w:c + 1] not in dict:
            dict[msg[w:c + 1]] = len(dict) + 1
            answer.append(dict[msg[w:c]])
            w = c

    return answer

msg_1 = 'KAKAO'
msg_2 = 'TOBEORNOTTOBEORTOBEORNOT'
msg_3 = 'ABABABABABABABAB'

print(solution(msg_1))
print(solution(msg_2))
print(solution(msg_3))

'''
먼저 대문자 알파벳 별로 값을 가지는 dictionary 만든 후
msg의 첫 번째 문자열 값을 compress_str변수에 저장한 후
'KAKAO'의 경우
'K' ... dictionary에 있으니 answer list에 'K' value값 추가 후
'KA' ... dictionary에 없으므로 dictionary에 27
'A'... dictionary에 있으니 answer list에 'A' value값 추가
이런 식으로 생각
----------------------------------------------------------
현재 글자 + 다음 글자가 dictionary에 있는지 없는지로 나눠서 
풀어야 한다.
현재 글자 + 다음 글자가 dictionary에 없으면 w = c, c = c + 1
현재 글자 + 다음 글자가 dictionary에 없으면 w는 변화없음, c = c + 1
'''
def solution_mine(msg):
    answer = []

    dict = {chr(64 + i): i for i in range(1, 26)}
    compress_str = msg[0]
    if compress_str in dict.keys():
        answer.append(dict[compress_str])

    for i in range(1, len(msg)):
        compress_str += msg[i]
        if msg[i] in dict.keys():
            answer.append(dict[msg[i]])

        if compress_str not in dict.keys():
            dict[compress_str] = len(dict.keys()) + 2
            compress_str = compress_str[1:]

    return answer

def solution_other(msg):
    answer = []

    tmp = {chr(e + 64) : e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer

print(solution_other(msg_1))
print(solution_other(msg_2))
print(solution_other(msg_3))