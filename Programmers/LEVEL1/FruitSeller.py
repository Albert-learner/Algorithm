# Restart 1. 과일장수

def solution(k, m, score):
    answer = 0

    score_sort = sorted(score, reverse = True)
    for box_cnt in range(0, len(score_sort), m):
        one_box = score_sort[box_cnt:box_cnt + m]
        if len(one_box) == m:
            answer += min(one_box) * m

    return answer

k_1 = 3
k_2 = 4

m_1 = 4
m_2 = 3

score_1 = [1, 2, 3, 1, 2, 3, 1]
score_2 = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(k_1, m_1, score_1))
print(solution(k_2, m_2, score_2))

def solution_best(k, m, score):
    answer = sum(sorted(score)[len(score) % m::m]) * m

    return answer

print(solution_best(k_1, m_1, score_1))
print(solution_best(k_2, m_2, score_2))