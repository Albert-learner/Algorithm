# 23. 튜플

def solution(s):
    answer = []

    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)

    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

s_1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s_2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s_3 = "{{20,111},{111}}"
s_4 = "{{123}}"
s_5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

# print(solution(s_1))
# print(solution(s_2))
# print(solution(s_3))
# print(solution(s_4))
# print(solution(s_5))

'''순서를 고려하지 않은 풀이'''
def solution_mine(s):
    answer = []

    answer = list(map(int, list(set(s.replace('{', '').replace('}', '').split(',')))))
    return answer

# print(solution_mine(s_1))
# print(solution_mine(s_2))
# print(solution_mine(s_3))
# print(solution_mine(s_4))
# print(solution_mine(s_5))

'''Counter객체와 정규표현식 이용한 풀이'''
import re
from collections import Counter

def solution_best(s):
    answer = []

    s_counter = Counter(re.findall('\d+', s))
    answer = list(map(int, [k for k, v in sorted(s_counter.items(),
                                                 key = lambda x : x[1],
                                                 reverse = True)]))
    return answer

print(solution_best(s_1))
print(solution_best(s_2))
print(solution_best(s_3))
print(solution_best(s_4))
print(solution_best(s_5))