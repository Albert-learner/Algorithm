# 18. 스타 수열

'''
원소의 개수가 가장 많은 것이 모든 부분 수열 중 가장 길이가 긴 스타 수열
만들 수 있음
x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1]와
{1,2}, {1,3}, {4,1}, {1,3} 의 교집합은 {1} 이고,
각 집합 내의 숫자들이 서로 다른 것 주의!!!
'''
from collections import Counter
def solution(a):
    answer = -1

    elements = Counter(a)
    for k in elements.keys():
        if elements[k] <= answer:
            continue

        common_cnt = 0
        idx = 0
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx + 1] != k) or (a[idx] == a[idx + 1]):
                idx += 1
                continue
            common_cnt += 1
            idx += 2
        answer = max(common_cnt, answer)

    if answer == -1:
        answer = 0
    else:
        answer *= 2

    return answer

a_1 = [0]
a_2 = [5, 2, 3, 3, 5, 3]
a_3 = [0, 3, 3, 0, 7, 2, 0, 2, 2, 0]

# print(solution(a_1))
# print(solution(a_2))
# print(solution(a_3))

def solution_other(a):
    answer = -1

    if len(a) % 2 != 0 or len(a) < 2:
        answer = 0

    counter = Counter(a)
    for key, val in counter.items():
        if counter[key] * 2 < answer:
            continue

        max_val, idx = key, 0
        length = 0
        while idx < len(a) - 1:
            if (a[idx] != max_val and a[idx + 1] != max_val) or a[idx] == a[idx + 1]:
                idx += 1
                continue

            length += 2
            idx += 2

        answer = max(answer, length)

    return answer

# print(solution_other(a_1))
# print(solution_other(a_2))
# print(solution_other(a_3))

# 유사 딕셔너리
from collections import defaultdict
def solution_best(a):
    answer = 0

    dic = defaultdict(list)
    for i, v in enumerate(a):
        dic[v].append(i)

    l = len(a)
    for k, v in dic.items():
        if len(v) <= answer // 2:
            continue
        else:
            now = a.copy()
            cnt = 0
            for j in v:
                if j > 0 and now[j - 1] != k:
                    now[j - 1] = k
                    cnt += 2
                elif j < l - 1 and now[j + 1] != k:
                    now[j + 1] = k
                    cnt += 2
            answer = max(answer, cnt)

    return answer

# print(solution_best(a_1))
# print(solution_best(a_2))
# print(solution_best(a_3))