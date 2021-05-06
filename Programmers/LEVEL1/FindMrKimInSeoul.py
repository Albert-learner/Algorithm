# 17. 서울에서 김서방 찾기

def solution(seoul):
    answer = ''

    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer += '김서방은 ' + str(i) + '에 있다'

    return answer

seoul_1 = ['Jane', 'Kim']
print(solution(seoul_1))

def solution_best(seoul):
    answer = '김서방은 {}에 있다'.format(seoul.index('Kim'))

    return answer

print(solution_best(seoul_1))