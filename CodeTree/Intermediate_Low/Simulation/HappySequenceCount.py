n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# First Solution
def has_run(seq, m_cnts):
    run = 1

    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            run += 1
            if run >= m_cnts:
                return True
            else:
                run = 1

    return False if run < m_cnts else True

happy_seqs = 0
for row in grid:
    if has_run(row, m):
        happy_seqs += 1

for col in zip(*grid):
    if has_run(col, m):
        happy_seqs += 1

print(happy_seqs)

# # Second Solution
happy_seqs = 0

for row in grid:
    for i in range(n - m + 1):
        if row[i:i + m].count(row[i]) >= m:
            happy_seqs += 1
            break

for col in zip(*grid):
    for i in range(n - m + 1):
        if col[i:i + m].count(col[i]) >= m:
            happy_seqs += 1
            break

print(happy_seqs)

"""
3 2
1 2 2
1 3 4
1 2 3
=>
2
============
3 1
1 2 3
4 5 6
7 8 8
=>
6
"""
