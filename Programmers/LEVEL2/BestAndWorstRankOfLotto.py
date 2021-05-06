# 30. 로또의 최고 순위와 최저 순위

'''스스로 풀었지만 비효율적인 풀이'''
def solution(lottos, win_nums):
    answer = [7, 7]

    lottos.sort()
    win_nums.sort()

    for i in lottos:
        if i == 0:
            answer[0] -= 1
        else:
            for j in win_nums:
                if i == j:
                    answer[0] -= 1
                    answer[1] -= 1

    if answer[0] == 7:
        answer[0] -= 1
    if answer[1] == 7:
        answer[1] -= 1

    return answer

lottos_1 = [44, 1, 0, 0, 31, 25]
lottos_2 = [0, 0, 0, 0, 0, 0]
lottos_3 = [45, 4, 35, 20, 3, 9]

win_nums_1 = [31, 10, 45, 1, 6, 19]
win_nums_2 = [38, 19, 20, 40, 15, 25]
win_nums_3 = [20, 9, 3, 45, 4, 35]

# print(solution(lottos_1, win_nums_1))
# print(solution(lottos_2, win_nums_2))
# print(solution(lottos_3, win_nums_3))

def solution_best(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    match = 0
    for x in win_nums:
        if x in lottos:
            match += 1
    return [answer[cnt_0 + match], answer[match]]

print(solution_best(lottos_1, win_nums_1))
print(solution_best(lottos_2, win_nums_2))
print(solution_best(lottos_3, win_nums_3))