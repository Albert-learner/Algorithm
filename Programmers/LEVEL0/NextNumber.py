# Restart 21. 다음에 올 숫자

'''
Consider that common difference or common ratio be able to get a minus cost.
'''
def solution(common):
    answer = 0

    two_overlap_lst = []
    for idx in range(0, len(common) - 1):
        two_overlap_lst.append(common[idx:idx + 2])

    diff_lst = []
    for first, second in two_overlap_lst:
        diff_lst.append(second - first)

    if len(set(diff_lst)) == 1:
        answer = common[-1] + diff_lst[0]
    else:
        first, second = two_overlap_lst[0]
        common_ratio = second // first
        answer = common[-1] * common_ratio

    return answer

common_1 = [1, 2, 3, 4]
common_2 = [2, 4, 8]

print(solution(common_1))
print(solution(common_2))

def solution_best(common):
    answer = 0

    a, b, c = common[:3]
    if (b - a) == (c - b):
        answer = common[-1] + (b - a)
    else:
        answer = common[-1] * (b // a)
    return answer

print(solution_best(common_1))
print(solution_best(common_2))
