n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnts = 0

for i in range(n - 2):
    for j in range(n - 2):
        cnts = 0
        for row in grid[i:i + 3]:
            cnts += sum(row[j:j + 3])

        max_cnts = max(max_cnts, cnts)

print(max_cnts)

"""
3
1 0 1
0 1 0
0 1 0
=>
4
===============
5
0 0 0 1 1
1 0 1 1 1
0 1 0 1 0
0 1 0 1 0
0 0 0 1 1
=>
6
"""