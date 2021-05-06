# 4. 가장 큰 수
from itertools import permutations

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True)
    answer = str(int(''.join(numbers)))
    return answer

numbers_1 = [6, 10, 2]
numbers_2 = [3, 30, 34, 5, 9]

print(solution(numbers_1))
print(solution(numbers_2))

# 시간 초과 ... 일일이 다 조합 X
def solution_mine(numbers):
    answer = ''

    # [6, 10, 2] -> [(6, 10, 2), (6, 2, 10), ... (2, 10, 6)]
    cases = list(permutations(numbers, len(numbers)))

    # [(6, 10, 2)] -> '6102'
    cases_str = []
    for i in cases:
        str_i = ''
        for j in i:
            str_i += str(j)
        cases_str.append(str_i)
        str_i = ''

    cases_answer = [int(i) for i in cases_str]
    answer = str(max(cases_answer))
    return answer

# print(solution_mine(numbers_1))
# print(solution_mine(numbers_2))