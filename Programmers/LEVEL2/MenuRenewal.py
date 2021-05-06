# 20. 메뉴 리뉴얼

from collections import Counter
from itertools import  combinations
# 조합을 먼저 한 후 개수를 센다.
def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            tmp += comb
        counters = Counter(tmp)
        print(counters)
        if len(counters) != 0 and max(counters.values()) != 1:
            answer += [''.join(count) for count in counters
                              if counters[count] == max(counters.values())]

    answer = sorted(answer)
    return answer

orders_1 = ['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH']
orders_2 = ['ABCDE', 'AB', 'CD', 'ADE', 'XYZ', 'XYZ', 'ACD']
orders_3 = ['XYZ', 'XWY', 'WXA']

course_1 = [2, 3, 4]
course_2 = [2, 3, 5]
course_3 = [2, 3, 4]

# print(solution(orders_1, course_1))
# print(solution(orders_2, course_2))
# print(solution(orders_3, course_3))

def solution_best(orders, course):
    answer = []

    for c in course:
        order_comb = []
        for order in orders:
            order_comb += combinations(sorted(order), c)

        most_ordered = Counter(order_comb).most_common()
        answer += [comb for comb, cnt in most_ordered
                   if cnt > 1 and cnt == most_ordered[0][1]]

    answer = [''.join(pair) for pair in sorted(answer)]

    return answer

print(solution_best(orders_1, course_1))
print(solution_best(orders_2, course_2))
print(solution_best(orders_3, course_3))

'''개수를 먼저 세고 조합을 하려니 안 되지....'''
def solution_mine(orders, course):
    answer = []

    counters = Counter()
    for order in orders:
        counters += Counter(order)

    counters_lst = sorted([tuple(item) for item in counters.items()],
                          key=lambda x: x[1], reverse=True)

    # answer_counters = Counter()
    # for items in course:
    #     answer_counters += counters.most_common(items)
    #     answer_counters += '\n'

    return answer

# print(solution_mine(orders_1, course_1))
# print(solution_mine(orders_2, course_2))
# print(solution_mine(orders_3, course_3))

