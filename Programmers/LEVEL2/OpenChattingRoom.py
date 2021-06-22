# 31. 오픈 채팅방

def solution(record):
    answer = []

    user_dict = {}
    for message in record:
        if (message.split()[0] == 'Enter') or (message.split()[0] == 'Change'):
            user_dict[message.split()[1]] = message.split()[2]

    for message in record:
        if message.split()[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(user_dict[message.split()[1]]))
        elif message.split()[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(user_dict[message.split()[1]]))
        else:
            pass

    return answer

record_1 = ["Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan"]

print(solution(record_1))

'''
어떤 경우에 딕셔너리에 추가를 해야 하는지 생각을 잘못함. 한 번에 다 생각하려고 하지 않기
'''
def solution_mine(record):
    answer = []

    message = [[reco.split()] for reco in record]
    message_dict = {}
    for person in message:
        if person[0][0] == 'Enter':
            if person[0][1] not in message_dict.keys():
                message_dict[person[0][1]] = person[0][2]
            else:
                message_dict[person[0][1]] = person[0][2]
                answer.append(str(person[0][2]) + '님이 들어왔습니다.')
        elif person[0][0] == 'Leave':
            if person[0][1] in message_dict.keys():
                answer.append(str(message_dict[person[0][1]]) + '님이 나갔습니다.')
        else:
            if person[0][1] in message_dict.keys():
                message_dict[person[0][1]] = person[0][2]
                answer.append(str(person[0][2]) + '님이 들어왔습니다.')

    return answer

# print(solution_mine(record_1))

def solution_other(record):
    answer = []

    namespace = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
    return answer

# print(solution_other(record_1))

def solution_best(records):
    user_id = {EC.split()[1]: EC.split()[-1] for EC in records if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.'
            for E_L in records if not E_L.startswith('Change')]

# print(solution_best(record_1))
'''
처음 풀이하는데 있어서 Enter에 대해 먼저 dict를 만들고 Change에 대해 dict를 만들어서 에러가 발생
다음 반례를 생각해보길,
1.prodo 입장 ->
2.prodo에서 ryan으로 Change ->
3.prodo 퇴장 ->
4.prodo로 재입장

return ['prodo 입장','prodo 퇴장','prodo 입장']

Change가 최종적인 닉네임이 아님,,
재입장시에도 닉네임변경이 가능하다는 것을 배제하고 풀어서 틀린 것.
'''
