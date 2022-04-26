# 7주차 2번 점프 게임

def solution(nums):
    answer = False

    for idx, num in enumerate(nums):
        if num == 0:
            continue

        if idx - num >= 0 and nums[idx - num] == 0:
            return True
        if idx + num < len(nums) and nums[idx + num] == 0:
            return True

    return answer

nums_1 = [2, 3, 1, 1, 4]
nums_2 = [3, 2, 1, 0, 4]
nums_3 = [2, 5, 0, 0]
nums_4 = [0, 2, 3]
nums_5 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
nums_6 = [2, 0]
nums_7 = [2, 0, 0]
nums_8 = [0]
nums_9 = [3, 1, 2, 1, 4]
nums_10 = [2, 0, 0, 5]

print(solution(nums_1))
print(solution(nums_2))
print(solution(nums_3))
print(solution(nums_4))
print(solution(nums_5))
print(solution(nums_6))
print(solution(nums_7))
print(solution(nums_8))
print(solution(nums_9))
print(solution(nums_10))