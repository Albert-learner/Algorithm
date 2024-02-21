# 1002 터렛

"""
This is about mathematic problem. The conception is the distance between two circle's center.
"""
T = int(input())
pos_info = [list(map(int, input().split())) for _ in range(T)]

for x1, y1, r1, x2, y2, r2 in pos_info:
    distance_between_centers = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if distance_between_centers == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance_between_centers or r1 + r2 == distance_between_centers:
        print(1)
    elif abs(r1 - r2) < distance_between_centers < (r1 + r2):
        print(2)
    else:
        print(0)

"""
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
=>
2
1
0
"""