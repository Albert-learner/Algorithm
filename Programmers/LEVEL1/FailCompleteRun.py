# 12. 완주하지 못한 선수

def solution(participant, completion):
    answer = ''

    # 이름 순서대로 정렬
    participant.sort()
    completion.sort()

    global i

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

    answer = participant[i + 1]
    return answer


participant_1 = ['leo', 'kiki', 'eden']
participant_2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
participant_3 = ['mislav', 'stanko', 'mislav', 'ana']

completion_1 = ['eden', 'kiki']
completion_2 = ['josipa', 'filipa', 'marina', 'nikola']
completion_3 = ['stanko', 'ana', 'mislav']

print(solution(participant_1, completion_1))
print(solution(participant_2, completion_2))
print(solution(participant_3, completion_3))


import collections

def solution_best(participant, completion):
    answer_counter = collections.Counter(participant) - collections.Counter(completion)
    answer = list(answer_counter.keys())[0]

    return answer

# print(solution_best(participant_1, completion_1))
# print(solution_best(participant_2, completion_2))
# print(solution_best(participant_3, completion_3))