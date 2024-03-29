# 시소 짝궁

"""
I didn't solve this problem by myself. The key of this problem is not using 2 loop.
And divide pairs and possibles of balanced position.
See it again.
"""
from collections import Counter
def solution(weights):
    answer = 0

    cntr = Counter(weights)
    for weight, weight_cnts in cntr.items():
        if weight_cnts >= 2:
            answer += weight_cnts * (weight_cnts - 1) // 2

    weights = set(weights)
    for weight in weights:
        if weight * (2/3) in weights:
            answer += cntr[weight * (2/3)] * cntr[weight]
        if weight * (2/4) in weights:
            answer += cntr[weight * (2/4)] * cntr[weight]
        if weight * (3/4) in weights:
            answer += cntr[weight * (3/4)] * cntr[weight]

    return answer

weights_1 = [100, 180, 360, 100, 270]

print(solution(weights_1))