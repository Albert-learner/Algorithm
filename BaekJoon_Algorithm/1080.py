# 1080. 행렬

"""
I didn't solve this problem by myself. The key of this problem is comparing first element of two marices.
And the last key is that impossible changes of two matrices.
See it again.
"""
# 1. My Solution(practice)
N, M = map(int, input().split())
matrix_A = [list(map(int, list(input()))) for _ in range(N)]
matrix_B = [list(map(int, list(input()))) for _ in range(N)]

def convert(i, j):
    for r in range(i, i + 3):
        for c in range(j, j + 3):
            if matrix_A[r][c] == 0:
                matrix_A[r][c] = 1
            else:
                matrix_A[r][c] = 0

min_cnts = 0
if N >= 3 and M >= 3:
    for row in range(N - 2):
        for col in range(M - 2):
            if matrix_A[row][col] != matrix_B[row][col]:
                min_cnts += 1
                convert(row, col)
else:
    min_cnts = -1

if min_cnts != -1:
    if matrix_A != matrix_B:
        min_cnts = -1

print(min_cnts)

# 2. Not my Solution
n, m = map(int, input().split())
listA = []
for _ in range(n): # 리스트A 선언
    listA.append(list(map(int, list(input()))))
listB = []
for _ in range(n): # 리스트B 선언
    listB.append(list(map(int, list(input()))))


def check(i, j): # 뒤집기 함수
    for x in range(i, i+3):
        for y in range(j, j+3):
            if listA[x][y] == 0:
                listA[x][y] = 1
            else:
                listA[x][y] = 0


cnt = 0 # 카운트
if (n < 3 or m < 3) and listA != listB:
    # 예외 1, 리스트가 작을 때
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                check(r, c)

if cnt != -1:
    if listA != listB: # A와 B가 같은지 확인
        cnt = -1
print(cnt)

"""
3 4
0000
0010
0000
1001
1011
1001
=>
2
===========
3 3
111
111
111
000
000
000
=>
1
===========
1 1
1
0
=>
-1
===========
18 3
001
100
100
000
011
010
100
100
010
010
010
110
101
101
000
110
000
110
001
100
011
000
100
010
011
100
101
101
010
001
010
010
111
110
111
001
=>
7
"""