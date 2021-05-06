# 5. 두 개 뽑아서 더하기
from itertools import combinations

def solution(numbers):
    answer = []

    # 조합의 리스트 -> [(2, 1), (2, 3), (2, 4), (2, 1), (1, 3), (1, 4), (1, 1), (3, 4), (3, 1), (4, 1)]
    combinations_lst = list(combinations(numbers, 2))
    # print(combinations_lst)

    for pair in combinations_lst:
        answer.append(pair[0] + pair[1])

    answer = list(set(answer))
    answer.sort()
    return answer

numbers_1 = [2, 1, 3, 4, 1]
numbers_2 = [5, 0, 2, 7]

print(solution(numbers_1))
print(solution(numbers_2))

def solution_other(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = sorted(list(set(answer)))
    return answer

print(solution_other(numbers_1))
print(solution_other(numbers_2))