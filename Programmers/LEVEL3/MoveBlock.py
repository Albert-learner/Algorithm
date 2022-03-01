# 28. 블록 이동하기

from collections import deque
def move_possible(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    # 평행이동
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in DELTAS:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and \
            new_board[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1, nxt2))

    # 회전
    # 가로 방향일 떄
    if cur1[Y] == cur2[Y]:
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[Y] + d][cur1[X]] == 0 and \
                    new_board[cur2[Y] + d][cur2[X]] == 0:
                cand.append((cur1, (cur1[Y] + d, cur1[X])))
                cand.append((cur2, (cur2[Y] + d, cur2[X])))
    # 새로 방향일 때
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X] + d] == 0 and \
                new_board[cur2[Y]][cur2[X] + d] == 0:
                cand.append(((cur1[Y], cur1[X] + d), cur1))
                cand.append(((cur2[Y], cur2[X] + d), cur2))

    return cand

def solution(board):
    answer = -1

    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = {((1, 1), (1, 2))}

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            answer = count
            return answer
        for nxt in move_possible(cur1, cur2, new_board):
            if nxt not in confirm:
                que.append((*nxt, count + 1))
                confirm.add(nxt)

    return answer

board_1 = [
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 0],
           [0, 1, 0, 1, 1],
           [1, 1, 0, 0, 1],
           [0, 0, 0, 0, 0]
           ]

# print(solution(board_1))

'''
두 번째 풀이 ... 첫번째와 비슷함
'''
from collections import deque
def getNewPos(pos, board):
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    newPos = []
    y1, x1 = pos[0]
    y2, x2 = pos[1]
    # 상하좌우 이동
    for dy, dx in dir:
        if board[y1 + dy][x1 + dx] == 0 and board[y2 + dy][x2 + dx] == 0:
            newPos.append({(y1 + dy, x1 + dx), (y2 + dy, x2 + dx)})
    # 가로 -> 세로
    if y1 == y2:
        for dy, dx in dir[1::2]:
            if board[y1 + dy][x1 + dx] == 0 and board[y2 + dy][x2 + dx] == 0:
                newPos.append({(y1, x1), (y1 + dy, x1)})
                newPos.append({(y2, x2), (y2 + dy, x2)})
    # 세로 -> 가로
    else:
        for dy, dx in dir[::2]:
            if board[y1 + dy][x1 + dx] == 0 and board[y2 + dy][x2 + dx] == 0:
                newPos.append({(y1, x1), (y1, x1 + dx)})
                newPos.append({(y2, x2), (y2, x2 + dx)})
    return newPos

def solution_other(board):
    answer = -1

    n = len(board)
    board = [[1] + b + [1] for b in board]
    board = [[1] * (n + 2)] + board + [[1] * (n + 2)]
    pos = {(1, 1), (1, 2)}
    q = deque()
    visited = []
    q.append([pos, 0])
    visited.append(pos)
    while q:
        pos, distance = q.popleft()
        distance += 1
        for newPos in getNewPos(list(pos), board):
            if (n, n) in newPos:
                answer = distance
                return answer
            if newPos not in visited:
                q.append([newPos, distance])
                visited.append(newPos)
    return answer

print(solution_other(board_1))