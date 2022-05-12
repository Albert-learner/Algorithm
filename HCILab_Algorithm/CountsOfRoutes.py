# 10주차 20220523 길갯수

def solution(m, n):
    answer = 0

    routes = [[1] * n for _ in range(m)]
    for row in range(1, m):
        for col in range(1, n):
            routes[row][col] = routes[row - 1][col] + routes[row][col - 1]

    answer = routes[m - 1][n - 1]
    return answer

m_1 = 3
m_2 = 7
m_3 = 11
m_4 = 9
m_5 = 19
m_6 = 1
m_7 = 5
m_8 = 4

n_1 = 2
n_2 = 3
n_3 = 5
n_4 = 11
n_5 = 13
n_6 = 1
n_7 = 5
n_8 = 7

print(solution(m_1, n_1))
print(solution(m_2, n_2))
print(solution(m_3, n_3))
print(solution(m_4, n_4))
print(solution(m_5, n_5))
print(solution(m_6, n_6))
print(solution(m_7, n_7))
print(solution(m_8, n_8))