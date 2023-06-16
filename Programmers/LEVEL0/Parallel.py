# Restart 26. 평행

from itertools import combinations
def solution(dots):
    answer = 0

    # Find 4 dots combination
    dots_comb = list(combinations(dots, 2))

    # Find line combination that satisfy [a-b, c-d], [a-c, b-d], [a-d, b-c]
    lines_comb = [(dots_comb[line_idx], dots_comb[-line_idx - 1]) for line_idx in range(len(dots_comb) // 2)]

    for two_lines in lines_comb:
        first_line, second_line = two_lines
        (first_front_x, first_front_y), (first_rear_x, first_rear_y) = first_line
        (second_front_x, second_front_y), (second_rear_x, second_rear_y) = second_line
        first_grad = (first_rear_y - first_front_y) / (first_rear_x - first_front_x)
        second_grad = (second_rear_y - second_front_y) / (second_rear_x - second_front_x)

        if first_grad == second_grad:
            answer = 1


    return answer

dots_1 = [[1, 4], [9, 2], [3, 8], [11, 6]]
dots_2 = [[3, 5], [4, 1], [2, 4], [5, 10]]

print(solution(dots_1))
print(solution(dots_2))

'''
Weird about confusing Problem's explanation
a, b, c, d
[a-b], [a-c], [a-d], [b-c], [b-d], [c-d] -> not apply combination 2
'''
def solution_mine(dots):
    answer = 0

    dots_comb = list(combinations(dots, 2))
    print(dots_comb)
    grad_lst = []
    for two_points in dots_comb:
        (first_x, first_y), (last_x, last_y) = two_points
        gradient = (last_y - first_y) / (last_x - first_x)
        grad_lst.append(gradient)

    if len(grad_lst) != len(set(grad_lst)):
        answer = 1
    else:
        answer = 0

    return answer

# print(solution_mine(dots_1))
# print(solution_mine(dots_2))

def solution_other(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    answer1 = ((y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2))
    answer2 = ((y1 - y3) * (x2 - x4) == (y2 - y4) * (x1 - x3))
    answer3 = ((y1 - y4) * (x2 - x3) == (y2 - y3) * (x1 - x4))

    return 1 if answer1 or answer2 or answer3 else 0

from functools import reduce
def solution_best(dots):
    return int(max(reduce(lambda dict, x: dict.update({x: dict.get(x, 0)+1}) or dict,[(d1[1] - d2[1]) / (d1[0] - d2[0]) if d1[0] - d2[0] else "x" for d1 in dots for d2 in dots if not d1 == d2], {}).values()) > 2)
