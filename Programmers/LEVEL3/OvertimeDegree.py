# 6. 야근 지수

'''
효율성 때문에 heap으로 풀어야 함.
'''
import heapq as hq
def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0

    works = [-i for i in works]
    hq.heapify(works)
    for _ in range(n):
        w = hq.heappop(works) + 1
        hq.heappush(works, w)

    answer = sum([i ** 2 for i in works])
    return answer

n_1 = 4
n_2 = 1
n_3 = 3

works_1 = [4, 3, 3]
works_2 = [2, 1, 2]
works_3 = [1, 1]

print(solution(n_1, works_1))
print(solution(n_2, works_2))
print(solution(n_3, works_3))

'''
accuracy도 틀리고, 효율성도 틀린 풀이
'''
def solution_mine(n, works):
    answer = 0

    if sum(works) < n:
        answer = 0
    else:
        if len(works) < n:
            diff = n - len(works)
            for i in range(len(works)):
                works[i] -= 1

            for i in range(diff):
                works[i] -= 1
        else:
            for i in range(n):
                works[i] -= 1

        answer = sum([i ** 2 for i in works])
    return answer

# print(solution_mine(n_1, works_1))
# print(solution_mine(n_2, works_2))
# print(solution_mine(n_3, works_3))

'''
정렬해서 풀어봤자 26점 정도...
'''
def solution_mine2(n, works):
    answer = 0

    if sum(works) < n:
        answer = 0
    else:
        works.sort(reverse=True)
        if len(works) < n:
            diff = n - len(works)
            for i in range(len(works)):
                works[i] -= 1

            for i in range(diff):
                works[i] -= 1
        else:
            for i in range(n):
                works[i] -= 1

        answer = sum([i ** 2 for i in works])
    return answer

# print(solution_mine2(n_1, works_1))
# print(solution_mine2(n_2, works_2))
# print(solution_mine2(n_3, works_3))

'''
이렇게 풀면 안 됨... 효율성 탈락
'''
def solution_bad(n, works):
    answer = 0

    if sum(works) < n:
        return 0

    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1
    answer = sum([w ** 2 for w in works])
    return answer

# print(solution_bad(n_1, works_1))
# print(solution_bad(n_2, works_2))
# print(solution_bad(n_3, works_3))

