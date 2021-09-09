# 10. 숫자 게임

'''
규칙을 어느 정도 파악했으나 한끗 차이로... j변수
'''
def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer += 1
            j += 1

    return answer

A_1 = [5, 1, 3, 7]
A_2 = [2, 2, 2, 2]

B_1 = [2, 2, 6, 8]
B_2 = [1, 1, 1, 1]

print(solution(A_1, B_1))
print(solution(A_2, B_2))

def solution_other(A, B):
    answer = 0

    A.sort(reverse = True)
    B.sort(reverse = True)

    for num_A in A:
        Min = num_A
        for i in range(len(B)):
            if Min < B[i]:
                Min = B[i]
            else:
                break

        if Min == num_A:
            continue
        else:
            B.remove(Min)
            answer += 1
    return answer

print(solution_other(A_1, B_1))
print(solution_other(A_2, B_2))