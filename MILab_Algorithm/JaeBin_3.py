# 3. 선 긋기

draw_cnt = int(input())
point = []
line_length = 0

for t in range(1, draw_cnt+1):
    point_1, point_2 = map(int, input().split())
    if point_1 > point_2:
        point_1, point_2 = point_2, point_1
    else:
        tup_point = (point_1, point_2)
        point.append(tup_point)

point.sort()
left = point[0][0]
right = point[0][1]

for i in range(1, draw_cnt):
    if point[i][0] <= right:
        right = max(point[i][1], right)
    else:
        line_length += right - left
        left = point[i][0]
        right = point[i][1]

line_length += right - left
print(line_length)

# 내 풀이 ...틀렸네 순서가 다르면 어떻게 할건데??
# draw_cnt = int(input())
# last_point = 0
# line_length = 0
# line = []
# for t in range(1, draw_cnt+1):
#     point_1, point_2 = map(int, input().split())
#     if t == 1:
#         line_length = point_2 - point_1
#         last_point = point_2
#     else:
#         if point_1 < last_point:
#             if point_2 == last_point:
#                 continue
#             else:
#                 diff_length = point_2 - last_point
#                 line_length += diff_length
#                 last_point = point_2
#         elif point_1 == last_point:
#             diff_length = point_2 - point_1
#             line_length += diff_length
#         else:
#             line.append(line_length)
#             line_length = point_2 - point_1
#
# line.append(line_length)
# print(sum(line))