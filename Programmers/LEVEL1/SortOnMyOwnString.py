# 16. 문자열 내 마음대로 정렬하기

# 내가 풀지 못했음... 왜 어렵게 생각했을까 ㅠㅠㅠ
def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    # print(strings)
    strings.sort()
    # print(strings)

    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer

strings_1 = ['sun', 'bed', 'car']
strings_2 = ['abce', 'abcd', 'cdx']

n_1 = 1
n_2 = 2

# print(solution(strings_1, n_1))
# print(solution(strings_2, n_2))

def solution_best(strings, n):
    answer = sorted(sorted(strings), key = lambda x : x[n])

    return answer

# print(solution_best(strings_1, n_1))
# print(solution_best(strings_2, n_2))