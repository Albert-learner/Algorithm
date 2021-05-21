# 36. 뉴스 클러스터링

# 집합으로 생각하면 안 되는 문제 ... 3번째 case
def solution(str1, str2):
    answer = 0

    str1_lst = []
    str2_lst = []

    # 'FR', 'RA', ...
    for s1, slice_s1 in zip(str1, str1[1:]):
        two_str = ''.join([s1, slice_s1])
        # '+' 기호 제거
        if two_str.isalpha():
            str1_lst.append(two_str.lower())

    for s2, slice_s2 in zip(str2, str2[1:]):
        two_str_1 = ''.join([s2, slice_s2])
        if two_str_1.isalpha():
            str2_lst.append(two_str_1.lower())

    if len(str1_lst) > len(str2_lst):
        intersection_sets = [str1_lst.remove(x) for x in str2_lst
                             if x in str1_lst]
    else:
        intersection_sets = [str2_lst.remove(x) for x in str1_lst
                             if x in str2_lst]

    union_sets = str1_lst + str2_lst
    union = len(union_sets)

    if union == 0:
        return 65536

    answer = int(len(intersection_sets) / union * 65536)
    return answer

str1_1 = 'FRANCE'
str1_2 = 'handshake'
str1_3 = 'aa1+aa2'
str1_4 = 'E=M*C^2'

str2_1 = 'french'
str2_2 = 'shake hands'
str2_3 = 'AAAA12'
str2_4 = 'e=m*c^2'

print(solution(str1_1, str2_1))
print(solution(str1_2, str2_2))
print(solution(str1_3, str2_3))
print(solution(str1_4, str2_4))

def solution_other(str1, str2):
    list_str1 = []
    list_str2 = []

    for s1, slice_s1 in zip(str1, str1[1:]):  # str1 문자만 2글자씩 뽑기
        join_str = "".join([s1, slice_s1])
        if join_str.isalpha():
            list_str1.append(join_str.lower())

    for s2, slice_s2 in zip(str2, str2[1:]):  # str2 문자만 2글자씩 뽑기
        join_str = "".join([s2, slice_s2])
        if join_str.isalpha():
            list_str2.append(join_str.lower())

    # print(list_str1)
    # print(list_str2)
    if len(list_str1) > len(list_str2):
        # 교집합의 개수를 구함
        inter = [list_str1.remove(x) for x in list_str2 if x in list_str1]
    else:
        inter = [list_str2.remove(x) for x in list_str1 if x in list_str2]

    # print(inter)
    # 합집합은 교집합 + 나머지 원소들
    list_uni = list_str1 + list_str2
    uni = len(list_uni)

    if uni == 0:
        return 65536

    return int(len(inter) / uni * 65536)

# print(solution_other(str1_1, str2_1))
# print(solution_other(str1_2, str2_2))
# print(solution_other(str1_3, str2_3))
# print(solution_other(str1_4, str2_4))

def solution_best(str1, str2):
    answer = 0

    str1_lst = [str1[i:i + 2].lower() for i in range(len(str1) - 1)
                if str1[i:i + 2].isalpha()]
    str2_lst = [str2[i:i + 2].lower() for i in range(len(str2) - 1)
                if str2[i:i + 2].isalpha()]

    intersections = 0
    unions = 0

    for s in set(str1_lst + str2_lst):
        unions += max(str1_lst.count(s), str2_lst.count(s))
        intersections += min(str1_lst.count(s), str2_lst.count(s))

    if unions == 0:
        return 65536

    answer = int(intersections / unions * 65536)
    return answer

# print(solution_best(str1_1, str2_1))
# print(solution_best(str1_2, str2_2))
# print(solution_best(str1_3, str2_3))
# print(solution_best(str1_4, str2_4))