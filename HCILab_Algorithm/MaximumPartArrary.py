# 10주차 20220523 최대 부분 배열

def solution(nums):
    answer = 0

    max_arr = [nums[0]]
    for i in range(1, len(nums)):
        max_arr.append(nums[i] + (max_arr[i - 1] if max_arr[i - 1] > 0 else 0))

    answer = max(max_arr)
    return answer

nums_1 = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [1, 2]
nums_3 = [-1]
nums_4 = [0, 3, -1]
nums_5 = [-2, -1]
nums_6 = [-9, 8, -7, 6, -5, 4, -3, 2, -1, 0]
nums_7 = [-5, -2, 8, 9]
nums_8 = [-5, 3, 9, -7]


print(solution(nums_1))
print(solution(nums_2))
print(solution(nums_3))
print(solution(nums_4))
print(solution(nums_5))
print(solution(nums_6))
print(solution(nums_7))
print(solution(nums_8))