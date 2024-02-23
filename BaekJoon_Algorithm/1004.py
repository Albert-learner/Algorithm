# 1004. 어린 왕자

"""
I was stuck about getting data. I need to study more about Python language.
And also the solution is unique because it requires mathematical thinking.
See it again.
"""
# 1. My Solution
T = int(input())
for _ in range(T):
    min_cnts = 0
    x1, y1, x2, y2 = map(int, input().split())
    planets = int(input())
    for planet in range(planets):
        cx, cy, r = map(int, input().split())
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        if (dist1 < r ** 2 and dist2 > r ** 2) or (dist1 > r ** 2 and dist2 < r ** 2):
            min_cnts += 1

    print(min_cnts)

# 2. Not my Solution
T = int(input())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    for i in range(N):
        cx, cy, r = map(int, input().split())
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2

        if (dist1 < r ** 2 and dist2 > r ** 2) or (dist1 > r ** 2 and dist2 < r ** 2):
            cnt += 1

    print(cnt)

"""
2
-5 1 12 1
7
1 1 8
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
-5 1 5 1
1
0 0 2
=>
3
0
==============
3
-5 1 5 1
3
0 0 2
-6 1 2
6 2 2
2 3 13 2
8
-3 -1 1
2 2 3
2 3 1
0 1 7
-4 5 1
12 1 1
12 1 2
12 1 3
102 16 19 -108
12
-107 175 135
-38 -115 42
140 23 70
148 -2 39
-198 -49 89
172 -151 39
-179 -52 43
148 42 150
176 0 10
153 68 120
-56 109 16
-187 -174 8
=>
2
5
3
"""