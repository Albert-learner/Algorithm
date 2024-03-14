# 1531. 투명

"""
I didn't solve this problem by myself. This is about simple implementation but I think too much.
See this again for simple implementation.
"""
# 1. My Solution
N, M = map(int, input().split())
points_info = [list(map(int, input().split())) for _ in range(N)]
picture = [[0] * 100 for _ in range(100)]

for x1, y1, x2, y2 in points_info:
    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            picture[row - 1][col - 1] += 1

picture_cnts = 0
for row in range(len(picture)):
    for col in range(len(picture[0])):
        if picture[row][col] > M:
            picture_cnts += 1

print(picture_cnts)

# # 2. Not my Solution
# N, M = map(int, input().split())
# li = [[0]*100 for _ in range(100)]
# for _ in range(N):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             li[i-1][j-1] += 1
# cnt = 0
# for i in range(100):
#     for j in range(100):
#         if li[i][j] > M:
#             cnt += 1
# print(cnt)

"""
3 1
21 21 80 80
41 41 60 60
71 71 90 90
=>
500

"""