# 25. 음양 더하기

def solution(absolutes, signs):
    answer = 0

    sum_lst = [absolutes[i] if signs[i] == True else -absolutes[i]
               for i in range(len(signs))]

    answer = sum(sum_lst)
    return answer

absolutes_1 = [4, 7, 12]
absolutes_2 = [1, 2, 3]

signs_1 = [True, False, True]
signs_2 = [False, False, True]

print(solution(absolutes_1, signs_1))
print(solution(absolutes_2, signs_2))