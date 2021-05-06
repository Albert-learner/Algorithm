# 24. 쿼드압축 후 개수 세기

'''재귀로 풀지 반복문으로 풀지 고민만 하고 코딩을 못하겠네... 결국 재귀로'''
def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def check(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    nn = n // 2
                    check(x, y, nn)
                    check(x, y + nn, nn)
                    check(x + nn, y, nn)
                    check(x + nn, y + nn, nn)
                    return
        answer[init] += 1

    check(0, 0, N)
    return answer

arr_1 = [[1, 1, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]
arr_2 = [[1, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 1],
         [0, 1, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 1, 1, 1]
         ]

# print(solution(arr_1))
# print(solution(arr_2))

'''다른 풀이 numpy모듈 이용'''
import numpy as np
def solution_best(arr):
    answer = [0, 0]

    # 재귀함수 구현
    def check(a):
        if np.all(a == 0): return np.array([1, 0])
        if np.all(a == 1): return np.array([0, 1])
        n = a.shape[0] // 2
        return check(a[:n, :n]) + check(a[n:, :n]) + check(a[:n, n:]) + check(a[n:, n:])

    answer = check(np.array(arr)).tolist()
    return answer

print(solution_best(arr_1))
print(solution_best(arr_2))