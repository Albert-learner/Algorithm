# 22. 입국심사

def solution(n, times):
    answer = 0

    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer

n_1 = 6

times_1 = [7, 10]

print(solution(n_1, times_1))