# 27. 폰캣몬

def solution(nums):
    answer = 0

    mine = [nums[0]]
    for one in nums:
        if len(mine) != len(nums) // 2:
            if one not in mine:
                mine.append(one)
        else:
            break

    answer = len(mine)
    return answer

nums_1 = [3, 1, 2, 3]
nums_2 = [3, 3, 3, 2, 2, 4]
nums_3 = [3, 3, 3, 2, 2, 2]

# print(solution(nums_1))
# print(solution(nums_2))
# print(solution(nums_3))

'''내 풀이'''
from itertools import combinations
def solution_mine(nums):
    answer = 0

    comb_nums = list(combinations(nums, len(nums) // 2))
    no_dup_comb_nums = sorted([set(item) for item in comb_nums], key=lambda x: len(x),
                              reverse=True)
    answer = len(no_dup_comb_nums[0])
    return answer

# print(solution_mine(nums_1))
# print(solution_mine(nums_2))
# print(solution_mine(nums_3))

def solution_best(nums):
    answer = min(len(nums) // 2, len(set(nums)))

    return answer

print(solution_best(nums_1))
print(solution_best(nums_2))
print(solution_best(nums_3))