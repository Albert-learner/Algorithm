# 3. 문자열 내림차순으로 배치하기

# 내 풀이
def solution(s):
    answer = ''

    s_lst = []

    for i in s:
        s_lst.append(i)

    s_lst.sort(reverse=True)
    for i in s_lst:
        answer += i
    return answer

s_1 = 'Zbcdefg'
print(solution(s_1))

def solution_best(s):

    return ''.join(sorted(list(s), reverse = True))

s_1 = 'Zbcdefg'
print(solution_best(s_1))