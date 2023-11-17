# Restart 44. 문자열 나누기

'''
Solve this problem by following the statements of problem.
But it's hard to implement for me. See this again.
Last condition is important.
'''
def solution(s):
    answer = 0

    first_alp = ''
    fir_alp_same_cnt = 0
    diff_cnt = 0
    for sub_s in s:
        if first_alp == '':
            first_alp = sub_s
            fir_alp_same_cnt = 1
            continue

        if first_alp == sub_s:
            fir_alp_same_cnt += 1
        else:
            diff_cnt += 1

        if fir_alp_same_cnt == diff_cnt:
            first_alp = ''
            fir_alp_same_cnt = 0
            diff_cnt = 0
            answer += 1

    if first_alp != '':
        answer += 1
    return answer

'''
This is completely different with Solution.
pointer index is the keypoint and last condition is important in here.
'''
def solution_best(s):
    answer = 0

    pointer = 0
    first_same_cnt = 0
    for sub_s_idx, sub_s in enumerate(s):
        first_same_cnt += 1 if s[pointer] == sub_s else -1
        if first_same_cnt == 0:
            answer += 1
            pointer = sub_s_idx + 1

    return answer + 1 if first_same_cnt else answer

s_1 = "banana"
s_2 = "abracadabra"
s_3 = "aaabbaccccabba"

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))

print(solution_best(s_1))
print(solution_best(s_2))
print(solution_best(s_3))