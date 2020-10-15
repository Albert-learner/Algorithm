# 38. 실패율

# 내 풀이 X ... 뭔가 어렵네...
def solution(N, stages):
    answer = []

    # 스테이지 도달한 플레이어 수 ... k
    success_players = len(stages)

    # 실패율 리스트
    failing_rate_lst = []

    for i in range(1, N + 1):
        # 스테이지 도달했으나 클리어하지 못한 플레이어 수
        failing_cnt = 0
        for j in range(len(stages)):
            if stages[j] == i:
                failing_cnt += 1

        if failing_cnt == 0:
            failing_rate_lst.append(0)
        else:
            failing_rate_lst.append(failing_cnt / success_players)
        success_players = success_players - failing_cnt

    failing_rate_reverse_sort = sorted(failing_rate_lst, reverse = True)
    # print(failing_rate_reverse_sort)

    for i in range(len(failing_rate_reverse_sort)):
        answer.append(failing_rate_lst.index(failing_rate_reverse_sort[i]) + 1)
        failing_rate_lst[failing_rate_lst.index(failing_rate_reverse_sort[i])] = 2

    return answer

N_1 = 5
N_2 = 4

stages_1 = [2, 1, 2, 6, 2, 4, 3, 3]
stages_2 = [4, 4, 4, 4, 4]

# print(solution(N_1, stages_1))
# print(solution(N_2, stages_2))

# 이중 리스트 풀이 ... [2, 1, 2, 6, 2, 4, 3, 3] -> [[1], [2, 2, 2], [3, 3], [4], [6]]
def solution_mine(N, stages):
    answer = []


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

print(solution_best(N_1, stages_1))
print(solution_best(N_2, stages_2))