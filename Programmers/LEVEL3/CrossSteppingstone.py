# 25. 징검다리 건너기

def solution(stones, k):
    answer = 0

    left, right = 1, 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    answer = left
    return answer

stones_1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

k_1 = 3

print(solution(stones_1, k_1))

def solution_error(stones, k):
    answer = 0

    while(True):
        answer += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1

        count = 0
        for stone in stones:
            if stone == 0:
                count += 1
                if count == k:
                    return answer
            else:
                count = 0

    return answer

print(solution_error(stones_1, k_1))
