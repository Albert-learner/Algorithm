# 56. 최댓값과 최솟값

def solution(s):
    answer = ''

    s_split = list(map(int, s.split()))
    answer += str(min(s_split)) + ' ' + str(max(s_split))
    return answer

s_1 = "1 2 3 4"
s_2 = "-1 -2 -3 -4"
s_3 = "-1 -1"

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))