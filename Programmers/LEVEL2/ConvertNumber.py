# 숫자 변환하기

"""
I didn't solve this problem by myself. I miss the key that this is about Search and BFS is appropriate for this problem.
But using Python's set is more efficient than using Python deque.
See it again.
"""
from collections import deque

def solution(x, y, n):
    answer = 0
    distances = [0 for _ in range(y + 1)]

    que = deque([x])
    if x == y:
        return 0

    while que:
        mx = que.popleft()
        for m_dir in range(3):
            if m_dir == 0:
                cur_x = mx + n
            if m_dir == 1:
                cur_x = mx * 2
            if m_dir == 2:
                cur_x = mx * 3

            if cur_x > y or distances[cur_x]:
                continue

            if cur_x == y:
                return distances[mx] + 1

            que.append(cur_x)
            distances[cur_x] = distances[mx] + 1

    return -1


x_1 = 10
x_2 = 10
x_3 = 2

y_1 = 40
y_2 = 40
y_3 = 5

n_1 = 5
n_2 = 30
n_3 = 4

print(solution(x_1, y_1, n_1))
print(solution(x_2, y_2, n_2))
print(solution(x_3, y_3, n_3))


def solution_best(x, y, n):
    answer = 0

    s = set()
    s.add(x)
    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i + n <= y:
                nxt.add(i + n)
            if i * 2 <= y:
                nxt.add(i * 2)
            if i * 3 <= y:
                nxt.add(i * 3)
        s = nxt
        answer += 1

    return answer


print(solution_best(x_1, y_1, n_1))
print(solution_best(x_2, y_2, n_2))
print(solution_best(x_3, y_3, n_3))