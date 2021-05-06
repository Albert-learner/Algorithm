# 12. 변장

# 내가 직접 풀지 못함
def solution(clothes):
    answer = 0

    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    answer = 1
    for cloth_cnt in clothes_dict.values():
        answer *= (cloth_cnt + 1)

    answer -= 1
    return answer

clothes_1 = [['yellow_hat', 'headgear'],
             ['blue_sunglasses', 'eyewear'],
             ['green_turban', 'headgear']
             ]
clothes_2 = [['crow_mask', 'face'],
             ['blue_sunglasses', 'face'],
             ['smoky_makeup', 'face']
             ]

print(solution(clothes_1))
print(solution(clothes_2))

'''
잘못 생각한 풀이
'''
from itertools import combinations
def solution_error(clothes):
    answer = 0

    # 총 옷 이름 개수
    clothes_names_cnt = len(set(cloth[0] for cloth in clothes))

    # 총 옷 종류 개수
    clothes_kinds_cnt = len(set([cloth[1] for cloth in clothes]))

    answer += clothes_names_cnt

    if clothes_kinds_cnt >= 2:
        clothes_comb = [[cloth1, cloth2] for cloth1, cloth2 in list(combinations(clothes, 2)) if cloth1[1] != cloth2[1]]
        answer += len(clothes_comb)
    return answer

# print(solution_error(clothes_1))
# print(solution_error(clothes_2))

'''
좋은 풀이
'''
from collections import Counter
from functools import reduce
def solution_best(clothes):
    answer = 0

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y : x * (y + 1) , cnt.values(), 1) - 1
    return answer

# print(solution_best(clothes_1))
# print(solution_best(clothes_2))