# 9. N-Queen

def possible(x, y, n, col):
    for i in range(x):
        if y == col[i] or abs(y - col[i]) == x - i:
            return False
    return True

def queen(x, n, col):
    if x == n:
        return 1

    count = 0

    for y in range(n):
        if possible(x, y, n, col):
            col[x] = y
            count += queen(x + 1, n, col)

    return count

def solution(n):
    answer = 0

    col = [0] * n
    answer = queen(0, n, col)
    return answer

n_1 = 4

print(solution(n_1))

def DFS(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i] - queen[row]) == row - i:
                break
        else:
            count += DFS(queen, row + 1, n)
    return count

def solution_good(n):
    return DFS([0] * n, 0, n)

# print(solution_good(n_1))

def solution_other(n):
    cases = [0]
    def dfs(queens, next_queen):
        if next_queen in queens:
            return

        for row, column in enumerate(queens):
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                return

        queens.append(next_queen)
        if len(queens) == n:
            cases[0] += 1
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen)

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)

    return cases[0]

# print(solution_other(n_1))