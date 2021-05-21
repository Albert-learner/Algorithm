# 38. 실패율

# 내 풀이
def solution(N, stages):
    answer = []

    # 실패율 딕셔너리
    result = {}

    # 도달한 플레이어 수 ... 매 단계마다 바뀔 수 있다
    denominator = len(stages)

    for stage in range(1, N + 1):
        if denominator != 0:
            fail_cnt = stages.count(stage)
            result[stage] = fail_cnt / denominator
            denominator -= fail_cnt
        else:
            result[stage] = 0

    answer = sorted(result, key=lambda x: result[x],
                    reverse = True)
    return answer

N_1 = 5
N_2 = 4

stages_1 = [2, 1, 2, 6, 2, 4, 3, 3]
stages_2 = [4, 4, 4, 4, 4]

# print(solution(N_1, stages_1))
# print(solution(N_2, stages_2))

# 이중 리스트 풀이 ... [2, 1, 2, 6, 2, 4, 3, 3] -> [[1], [2, 2, 2], [3, 3], [4], [6]]
from collections import Counter
def solution_mine(N, stages):
    answer = []

    # {'1' : 2, '2' : 3, ... }
    result = {str(i): 0 for i in range(N + 1)}
    for i in stages:
        if str(i) in result.keys():
            result[str(i)] += 1
        else:
            if i == N + 1:
                result[str(0)] += 1

    # 마지막까지 성공한 사람
    success = {'0': result['0']}
    del (result['0'])

    denominator = len(stages)
    failing_rate_lst = []
    for stage, cnt in result.items():
        failing_rate = 0
        if cnt != 0:
            failing_rate = cnt / denominator
            failing_rate_lst.append(failing_rate)
            denominator -= cnt
        else:
            failing_rate = 0
            failing_rate_lst.append(failing_rate)

    sort_failing_rate_lst = sorted(failing_rate_lst,
                                   reverse=True)
    answer = [sort_failing_rate_lst.index(i) + 1
              for i in failing_rate_lst]
    return answer

# print(solution_mine(N_1, stages_1))
# print(solution_mine(N_2, stages_2))

def solution_best(N, stages):
    answer = []

    # 실패율 딕셔너리
    result = {}

    # 스테이지에 도달한 플레이어 수 = success_players / denominator : 분모
    denominator = len(stages)

    for stage in range(1, N + 1):
        if denominator != 0:
            failing_count = stages.count(stage)
            result[stage] = failing_count / denominator
            denominator -= failing_count
        else:
            result[stage] = 0
    answer = sorted(result, key=lambda x: result[x], reverse=True)
    return answer
#
# print(solution_best(N_1, stages_1))
# print(solution_best(N_2, stages_2))


def solution_other(N, stages):
    answer = []
    _len = len(stages)
    _num = 0

    for x in range(1, N + 1):
        for y in stages:
            if x == y:
                _num += 1
        if _num > 0:
            answer.append(_num / _len)
            _len = _len - _num
            _num = 0
        else:
            answer.append(0)
    answer = sorted(range(len(answer)), key=lambda k: answer[k], reverse=True)
    answer = [x + 1 for x in answer]
    return answer

print(solution_other(N_1, stages_1))
print(solution_best(N_2, stages_2))