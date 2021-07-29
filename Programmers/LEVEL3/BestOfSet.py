# 2. 최고의 집합

'''
숫자 s를 자연수 n개로 표현하면서 '곱이 가장 큰 수'가 되도록 하려면, n개의 자연수 간에 차이가
적어야 한다.
ex) 7을 3개의 자연수로 표현?? -> (7 // 3 = 2) ... [2, 2, 2]
s를 n으로 나눈 나머지가 있을 수 있으니 문제에서 오름차순 정렬 만족시키기 위해 맨 뒷자리 수부터
1씩 더해준다.
'''
def solution(n, s):
    if n > s: return [-1]

    answer = []
    # s를 n으로 나눈 몫이 n개가 되도록 초기값 설정
    initial = s // n
    for _ in range(n):
        answer.append(initial)
    idx = -1
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1

    return answer

n_1 = 2
n_2 = 2
n_3 = 2

s_1 = 9
s_2 = 1
s_3 = 8

print(solution(n_1, s_1))
print(solution(n_2, s_2))
print(solution(n_3, s_3))

'''
시간 초과 ... 조합 개수가 3개 이상이면 아마 안 될 듯
'''
def solution_mine(n, s):
    answer = []

    multi_lst = [i for i in range(1, s)]
    multi_set = []
    if len(multi_lst) < 2:
        answer.append(-1)
        return answer
    else:
        if len(multi_lst) % 2 == 1:
            for i in range(len(multi_lst) // 2):
                two_set = [multi_lst[i], multi_lst[-1 - i]]
                multi_set.append(two_set)
            multi_set.append([multi_lst[len(multi_lst) // 2],
                              multi_lst[len(multi_lst) // 2]])
        else:
            for i in range(len(multi_lst) // 2):
                two_set = [multi_lst[i], multi_lst[-1 - i]]
                multi_set.append(two_set)

    multiply_lst = []
    for x, y in multi_set:
        multiply = x * y
        multiply_lst.append(multiply)
    answer = multi_set[multiply_lst.index(max(multiply_lst))]
    return answer

# print(solution_mine(n_1, s_1))
# print(solution_mine(n_2, s_2))
# print(solution_mine(n_3, s_3))

'''
중복조합을 이용해서 풀어본 풀이 ... 시간 초과(범위가 10,000 이상이면 조합 X
'''
from itertools import combinations_with_replacement
def solution_mine2(n, s):
    answer = []

    num_lst = [i for i in range(1, s)]
    if len(num_lst) < 2:
        answer.append(-1)
        return answer

    comb_lst = list(combinations_with_replacement(num_lst, n))
    multi_set = []
    for one_set in comb_lst:
        if sum(one_set) == s:
            multi_set.append(one_set)

    biggest_multiply = multi_set[0][0] * multi_set[0][1]
    answer = list(multi_set[0])
    for one_set in multi_set:
        if biggest_multiply < one_set[0] * one_set[1]:
            if len(answer) == 0:
                answer = list(one_set)
            else:
                answer.clear()
                answer = list(one_set)

    return answer

# print(solution_mine2(n_1, s_1))
# print(solution_mine2(n_2, s_2))
# print(solution_mine2(n_3, s_3))

'''
다른 사람 풀이
'''
def solution_other(n, s):
    answer = []

    a = int(s / n)
    if a == 0:
        return [-1]

    b = s % n
    for i in range(n - b):
        answer.append(a)
    for i in range(b):
        answer.append(a + 1)

    return answer

# print(solution_other(n_1, s_1))
# print(solution_other(n_2, s_2))
# print(solution_other(n_3, s_3))