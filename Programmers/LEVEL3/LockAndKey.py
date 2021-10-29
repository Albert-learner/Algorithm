# 17. 자물쇠와 열쇠

def rotation(arr):
    length = len(arr)
    rotate_key = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            rotate_key[j][length - 1 - i] = arr[i][j]

    return rotate_key

def check(startX, startY, key, lock, p_size, start, end):
    pad = [[0] * p_size for _ in range(p_size)]

    # 패딩 초기화
    for i in range(len(key)):
        for j in range(len(key)):
            pad[startX + i][startY + j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            pad[i][j] += lock[i - start][j - start]
            if pad[i][j] != 1:
                return False

    return True

def solution(key, lock):
    answer = False

    # lock의 시작점과 끝나는 지점
    start = len(key) - 1
    end = start + len(lock)

    # padding이 추가된 배열의 행, 열의 크기
    pad_size = len(lock) + start * 2

    # 4가지만 비교 0, 90, 180, 270
    for angle in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, pad_size, start, end):
                    return True
        key = rotation(key)
    return answer

key_1 = [
         [0, 0, 0],
         [1, 0, 0],
         [0, 1, 1]
         ]

lock_1 = [
          [1, 1, 1],
          [1, 1, 0],
          [1, 0, 1]
          ]

print(solution(key_1, lock_1))

# 행렬 회전 90도
import numpy as np
def rotation_np(arr, angle):
    rotate_key = np.rot90(arr, 3 - angle)

    return rotate_key

def rotate90(arr):
    return list(zip(*arr[::-1]))

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]

def check_other(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False

    return True

def solution_other(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]

    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # 모든 방향(0, 90, 180, 270)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)

                # lock 가능 check
                if check_other(board, M, N):
                    return True

                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)

    return False

print(solution_other(key_1, lock_1))