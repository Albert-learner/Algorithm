# 22. 순위 검색

'''안일하게 생각했다. 이진탐색으로 풀어야 하는 문제'''
from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []

    info_dict = defaultdict(list)
    for inf in info:
        inf = inf.split()
        inf_conditions = inf[:-1]
        inf_score = int(inf[-1])
        for i in range(5):
            for comb in combinations(inf_conditions, i):
                tmp_conditions = ''.join(comb)
                info_dict[tmp_conditions].append(inf_score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for que in query:
        que = que.split(' ')
        que_score = int(que[-1])
        que = que[:-1]

        for i in range(3):
            que.remove('and')
        while '-' in que:
            que.remove('-')
        tmp_q = ''.join(que)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= que_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer

info_1 = ["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"
          ]
query_1 = ["java and backend and junior and pizza 100",
           "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250",
           "- and backend and senior and - 150",
           "- and - and - and chicken 100",
           "- and - and - and - 150"
           ]

from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution_best(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]

# print(solution_best(info_1, query_1))

