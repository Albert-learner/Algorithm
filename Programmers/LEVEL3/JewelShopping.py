# 20. 보석 쇼핑

'''
두 개의 변수를 이용하여 최종적으로 종류가 다 찼을 때, 시작 변수를 움직여서 조건에 맞는 범위 찾기
'''
from collections import Counter
def solution(gems):
    answer = []

    shortest = len(gems) + 1
    start_p, end_p = 0, 0
    contained = {}
    counter_gems = Counter(gems)

    while end_p < len(gems):
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1

        end_p += 1

        if len(contained) == len(counter_gems):
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p + 1, end_p]
                    break
                else:
                    break
    return answer

gems_1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems_2 = ["AA", "AB", "AC", "AA", "AC"]
gems_3 = ["XYZ", "XYZ", "XYZ"]
gems_4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

# print(solution(gems_1))
# print(solution(gems_2))
# print(solution(gems_3))
# print(solution(gems_4))

'''
Counter객체에 비해 Set이 속도 측면에서 더 빠름
'''
def solution_other(gems):
    answer = []

    start_p, end_p = 0, 0
    shortest = len(gems) + 1
    contained = {}
    check_len = len(set(gems))

    while end_p < len(gems):
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1

        end_p += 1

        if len(contained) == check_len:
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p + 1, end_p]
                    break
                else:
                    break

    return answer

print(solution_other(gems_1))
print(solution_other(gems_2))
print(solution_other(gems_3))
print(solution_other(gems_4))


def solution_best(gems):
    answer = []

    size = len(set(gems))
    dic = {gems[0]:1}
    temp = [0, len(gems) - 1]
    start, end = 0, 0

    while (start < len(gems) and end < len(gems)):
        if len(dic) == size:
            if end - start < temp[1] - temp[0]:
                temp = [start, end]

            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break

            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    answer = [temp[0] + 1, temp[1] + 1]
    return answer

# print(solution_best(gems_1))
# print(solution_best(gems_2))
# print(solution_best(gems_3))
# print(solution_best(gems_4))