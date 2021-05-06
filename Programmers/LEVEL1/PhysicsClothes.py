# 6. 체육복

# 내 스스로 풀기 X
def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            continue

        for j in reserve:
            if j == i - 1:
                answer += 1
                reserve.remove(j)
                break
            elif j == i + 1:
                if j in lost:
                    break
                answer += 1
                reserve.remove(j)
                break

    return answer

n_1, lost_1, reserve_1 = 5, [2, 4], [1, 3, 5]
n_2, lost_2, reserve_2 = 5, [2, 4], [3]
n_3, lost_3, reserve_3 = 3, [3], [1]

# print(solution(n_1, lost_1, reserve_1))
# print(solution(n_2, lost_2, reserve_2))
# print(solution(n_3, lost_3, reserve_3))

def solution_best(n, lost, reserve):
    answer = 0

    # 전처리 -> 중복 학생도 체육복을 도난당할 수 있다는 것
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    # print('set_reserve : ', set_reserve)
    # print('set_lost : ', set_lost)

    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    answer = n - len(set_lost)
    return answer

print(solution_best(n_1, lost_1, reserve_1))
print(solution_best(n_2, lost_2, reserve_2))
print(solution_best(n_3, lost_3, reserve_3))