# 42. 이진 변환 반복하기

def solution(s):
    answer = []

    erase_cnt, bin_cnt = 0, 0
    while True:
        if s == '1':
            break

        erase_cnt += s.count('0')
        s = s.replace('0', '')

        s = bin(len(s))[2:]
        bin_cnt += 1

    answer = [bin_cnt, erase_cnt]
    return answer

s_1 = '110010101001'
s_2 = '01110'
s_3 = '1111111'

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))

'''
list로 풀려고 했는데 '0'을 지우는 부분에서 막힘
문자열 그대로로 풀어야 함.
'''
def solution_mine(s):
    answer = []

    s = [ch for ch in s]
    bin_cnt = 0
    trans_s = []
    while s.count('0') != 0:
        for ch in s:
            if ch == '0':
                s.remove(ch)
            trans_s.append(ch)
        len_trans_s = len(trans_s)
        bin_trans_s = bin(len_trans_s)
        bin_cnt += 1
    bin_trans_s = int(bin(len(s)), 2)

    answer.append([bin_cnt, bin_trans_s])
    return answer

# print(solution_mine(s_1))
# print(solution_mine(s_2))
# print(solution_mine(s_3))

def solution_best(s):
    bin_cnt, erase_cnt = 0, 0
    while s != '1':
        bin_cnt += 1
        num = s.count('1')
        erase_cnt += len(s) - num
        s = bin(num)[2:]

    return [bin_cnt, erase_cnt]

print(solution_best(s_1))
print(solution_best(s_2))
print(solution_best(s_3))