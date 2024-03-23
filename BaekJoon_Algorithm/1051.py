# 1051. 숫자 정사각형

"""
I almost solve this problem by myself. The key of this problem is finding 4 coordinates of square that satisfy same costs.
I miss the point that the possible length of square.
See it again.
"""
# 1. My Solution
N, M = map(int, input().split())
rectangle = [list(map(int, list(input()))) for _ in range(N)]
max_length = min(N, M)

def find_square(s):
    for i in range(N - s + 1):
        for j in range(M - s + 1):
            if rectangle[i][j] == rectangle[i][j + s - 1] == rectangle[i + s - 1][j] == rectangle[i + s -1][j + s - 1]:
                return True

    return False

for p_len in range(max_length, 0, -1):
    if find_square(p_len):
        print(p_len ** 2)
        break

# 2. Not my Solution
def find_squre(s):
    for i in range(N-s+1):
        for j in range(M-s+1):
            if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return True

    return False


N, M = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(N)]

size = min(N,M)

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k):
        print(k**2)
        break

"""
3 5
42101
22100
22101
=>
9
================
2 2
12
34
=>
1
================
2 4
1255
3455
=>
4
================
1 10
1234567890
=>
1
================
11 10
9785409507
2055103694
0861396761
3073207669
1233049493
2300248968
9769239548
7984130001
1670020095
8894239889
4053971072
=>
49
"""