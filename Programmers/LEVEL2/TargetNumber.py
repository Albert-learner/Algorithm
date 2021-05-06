# 13. 타겟 넘버

# 개념만 알겠고, 푸는 방법을 모르겠네...
'''
1. DFS(깊이 우선 탐색) 풀이법
'''
def dfs(array, numbers, target, size):
    answer = 0

    if len(array) == size:
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        A = numbers.pop(0)
        for i in [1, -1]:
            array.append(A * i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(A)

        return answer

def solution_dfs(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer

numbers_1 = [1, 1, 1, 1, 1]

target_1 = 3

# print(solution_dfs(numbers_1, target_1))

'''
2. 완전 탐색
'''
from itertools import product

def solution(numbers, target):
    answer = 0

    lst = [(x, -x) for x in numbers]
    s = list(map(sum, product(*lst)))
    answer = s.count(target)

    return answer

# print(solution(numbers_1, target_1))

'''
3. BFS(넓이 우선 탐색) 풀이
'''
import collections

def solution_bfs(numbers, target):
    answer = 0

    stack = collections.deque([(0, 0)])

    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
            else:
                number = numbers[num_idx]
                stack.append((current_sum + number, num_idx + 1))
                stack.append((current_sum - number, num_idx + 1))

    return answer

# print(solution_bfs(numbers_1, target_1))

'''
4. 재귀
'''
def solution_recursive(numbers, target):
    answer = 0

    if not numbers and target == 0:
        answer = 1
    elif not numbers:
        answer = 0
    else:
        answer = solution_recursive(numbers[1:], target - numbers[0] + solution_recursive(numbers[1:], target + numbers[0]))
    return answer

