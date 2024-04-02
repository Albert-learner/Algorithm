# PCCP 기출문제 1번 붕대 감기

"""
I solve this problem by myself. But it is not efficient method.
I follow the table in problem, but it requires efficient arrangement.
See other solution and try to solve like that.
See it again.
"""
# 1. My Solution
def solution(bandage, health, attacks):
    answer = 0

    cast_time, second_restore, extra_restore = bandage
    start_attack_times, damages = list(list(zip(*attacks))[0]), list(list(zip(*attacks))[1])
    table = [[health, 0, False]]
    for time in range(1, attacks[-1][0] + 1):
        cur_health, consecutive_success, attack = table[-1]

        if cur_health >= health:
            cur_health = health

        if time in start_attack_times:
            cur_health -= damages[start_attack_times.index(time)]
            consecutive_success = 0
            attack = True
            table.append([cur_health, consecutive_success, attack])
            continue

        consecutive_success += 1
        cur_health += second_restore

        if consecutive_success == cast_time:
            cur_health += extra_restore
            consecutive_success = 0

        if attack == True:
            attack = False

        if cur_health >= health:
            cur_health = health

        if cur_health <= 0:
            break

        table.append([cur_health, consecutive_success, attack])

    answer = table[-1][0]
    if answer <= 0:
        answer = -1

    return answer

def solution_other(bandage, health, attacks):
    answer = 0

    max_health = health
    start = 1
    for start_time, damage in attacks:
        max_health += ((start_time - start) // bandage[0]) * bandage[2] + (start_time - start) * bandage[1]
        start = start_time + 1
        if max_health >= health:
            max_health = health

        max_health -= damage
        if max_health <= 0:
            return -1

    answer = max_health
    return answer

bandage_1 = [5, 1, 5]
bandage_2 = [3, 2, 7]
bandage_3 = [4, 2, 7]
bandage_4 = [1, 1, 1]

health_1 = 30
health_2 = 20
health_3 = 20
health_4 = 5

attacks_1 = [[2, 10], [9, 15], [10, 5], [11, 5]]
attacks_2 = [[1, 15], [5, 16], [8, 6]]
attacks_3 = [[1, 15], [5, 16], [8, 6]]
attacks_4 = [[1, 2], [3, 2]]

# print(solution(bandage_1, health_1, attacks_1))
# print(solution(bandage_2, health_2, attacks_2))
# print(solution(bandage_3, health_3, attacks_3))
# print(solution(bandage_4, health_4, attacks_4))

print(solution_other(bandage_1, health_1, attacks_1))
# print(solution_other(bandage_2, health_2, attacks_2))
# print(solution_other(bandage_3, health_3, attacks_3))
# print(solution_other(bandage_4, health_4, attacks_4))