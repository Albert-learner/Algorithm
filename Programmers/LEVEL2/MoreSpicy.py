# 10. 더 맵게
import heapq as hq

def solution(scovile, K):
    answer = 0


    return answer

# 가장 작은 값을 생각하자!! ... 힙 안 쓰면 초과 걸리네
def solution_error(scovile, K):
    answer = 0

    scovile.sort(reverse = True)

    while scovile[len(scovile) - 1] < K:
        try:
            scovile.append(scovile.pop() + scovile.pop() * 2)
        except IndexError:
            answer = -1
            return answer
        answer += 1
    return answer

scovile_1 = [1, 2, 3, 9, 10, 12]
K_1 = 7

print(solution_error(scovile_1, K_1))

def solution_best(scovile, K):
    answer = 0

    heap = []
    for num in scovile:
        hq.heappush(heap, num)

    while heap[0] < K:
        try:
            hq.heappush(heap, hq.heappop(heap) + (hq.heappop(heap) * 2))
        except IndexError:
            answer = -1
            return answer
        answer += 1

    return answer

# print(solution_best(scovile_1, K_1))