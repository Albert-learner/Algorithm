# 51. N진수 게임

'''
진법 변환 어떻게 하는지 파악하는 것이 관건
'''
def convert(base, cost):
    rest = '0123456789ABCDEF'
    trans_str = ''

    if cost == 0:
        return '0'
    while cost > 0:
        trans_str = rest[cost % base] + trans_str
        cost = cost // base

    return trans_str

def solution(n, t, m, p):
    answer = ''

    total_trans_str = ''
    for i in range(t * m):
        total_trans_str += convert(n, i)

    for ch in range(p -1 , t * m, m):
        answer += total_trans_str[ch]

    return answer

n_1 = 2
n_2 = 16
n_3 = 16

t_1 = 4
t_2 = 16
t_3 = 16

m_1 = 2
m_2 = 2
m_3 = 2

p_1 = 1
p_2 = 1
p_3 = 2

print(solution(n_1, t_1, m_1, p_1))
print(solution(n_2, t_2, m_2, p_2))
print(solution(n_3, t_3, m_3, p_3))

def convert_recursive(num, base):
    T = '0123456789ABCDEF'
    q, r = divmod(num, base)

    if q == 0:
        return T[r]
    else:
        return convert_recursive(q, base) + T[r]

def solution_other(n, t, m, p):
    answer = ''

    total_str = ''
    for i in range(t * m):
        total_str += convert_recursive(i, n)

    for _ in range(t):
        answer += total_str[p - 1]
        p += m

    return answer

# print(solution_other(n_1, t_1, m_1, p_1))
# print(solution_other(n_2, t_2, m_2, p_2))
