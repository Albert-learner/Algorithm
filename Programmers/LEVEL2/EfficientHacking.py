# 효율적인 해킹

"""
I didn't solve this problem by myself. The key of this problem is sorting column and ascending sorting.
And get S_i with easy method. Think simple, not complicated.
See it again.
"""
def solution(data, col, row_begin, row_end):
    answer = 0

    table = sorted(data, key=lambda row: [row[col - 1], -row[0]])
    for i in range(row_begin, row_end + 1):
        result = 0
        for j in table[i - 1]:
            result += j % i

        answer = answer ^ result

    return answer

data_1 = [[2, 2, 6],
          [1, 5, 10],
          [4, 2, 9],
          [3, 8, 3]]

col_1 = 2

row_begin_1 = 2

row_end_1 = 3

print(solution(data_1, col_1, row_begin_1, row_end_1))

from functools import reduce

def solution_best(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    return reduce(lambda x, y: x ^ y,
                  [sum(map(lambda x: x % (i + 1), data[i])) for i in range(row_begin - 1, row_end)])

print(solution_best(data_1, col_1, row_begin_1, row_end_1))