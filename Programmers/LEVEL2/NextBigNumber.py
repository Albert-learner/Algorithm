# 27. 다음 큰 숫자

def solution(n):
    answer = 0

    bin_n = bin(n)
    one_cnt = 0
    for i in bin_n:
        if i == '1':
            one_cnt += 1

    while True:
        n += 1
        next_one_cnt = 0
        bin_n_next = bin(n)
        for i in bin_n_next:
            if i == '1':
                next_one_cnt += 1

        if one_cnt == next_one_cnt:
            answer = int(bin_n_next, 2)
            break

    return answer

n_1 = 78
n_2 = 15

# print(solution(n_1))
# print(solution(n_2))

def solution_best(n):
    answer = 0

    bin_n = bin(n)
    one_cnt = bin_n.count('1')

    while True:
        n += 1
        bin_n_next = bin(n)
        next_one_cnt = bin_n_next.count('1')

        if one_cnt == next_one_cnt:
            answer = int(bin_n_next, 2)
            break

    return answer

print(solution_best(n_1))
print(solution_best(n_2))