# 41. 후보키

'''
범위가 4개로만 국한되는건가? 아니다
전체 조합에서 조건에 만족하지 않는 조건들을 빼는 방식으로 푼다
'''
from itertools import combinations
def solution(relation):
    answer = 0

    cand_keys = []
    n_row, n_col = len(relation), len(relation[0])

    # 전체 조합
    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    # 유일성
    unique = []
    for keys in candidates:
        tmp = [tuple(item[key] for key in keys)
               for item in relation]
        if len(set(tmp)) == n_row:
            unique.append(keys)

    cand_keys = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                cand_keys.discard(unique[j])

    answer = len(cand_keys)
    return answer

relation_1 = [["100", "ryan", "music", "2"],
              ["200", "apeach", "math", "2"],
              ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"],
              ["500", "muzi", "music", "3"],
              ["600", "apeach", "music", "2"]
              ]

print(solution(relation_1))

def solution_other(relation):
    answer = 0
    cand_keys = []

    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in cand_keys:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                cand_keys.append(i)

    answer = len(cand_keys)
    return answer

print(solution_other(relation_1))


