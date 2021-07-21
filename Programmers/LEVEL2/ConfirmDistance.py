# 54. 거리두기 확인하기


size = 5
def valid(r, c):
    return -1 < r < size and -1 < c < size


def BFS_check(x, y, place):
    dist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dist:
        nx, ny = x + dx, y + dy
        if valid(nx, ny) and place[nx][ny] == 'P':
            return False

    dist = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in dist:
        nx, ny = x + dx, y + dy
        if valid(nx, ny) and place[nx][ny] == 'P' \
                and (place[x][ny] != 'X' or place[nx][y] != 'X'):
            return False

    dist = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    for dx, dy in dist:
        nx, ny = x + dx, y + dy
        if valid(nx, ny) and place[nx][ny] == 'P' and place[x + dx // 2][y + dy // 2] != 'X':
            return False

    return True

def solution(places):
    answer = []

    for place in places:
        flag = False
        for r, c in [(i, j) for i in range(5) for j in range(5)]:
            if place[r][c] == 'P':
                result = BFS_check(r, c, place)
                if not result:
                    answer.append(0)
                    flag = True
                    break

        if not flag:
            answer.append(1)

    return answer

places_1 = [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
            ]

# print(solution(places_1))

def solution_other(places):
    answer = []

    # place를 하나씩 확인
    for place in places:

        # 거리두기가 지켜지지 않음을 확인하면 바로 반복을 멈추기 위한 key
        key = False
        nowArr = []

        # 이번 place를 nowArr에 담아줍니다.
        for n in place:
            nowArr.append(list(n))

        # 이중 for문을 이용해 하나씩 확인합니다.
        for i in range(5):
            if key:
                break

            for j in range(5):
                if key:
                    break

                # 사람을 찾아내면 판단을 시작합니다.
                if nowArr[i][j] == "P":

                    if i + 1 < 5:
                        # 만약 바로 아랫부분에 사람이 존재하면 break
                        if nowArr[i + 1][j] == "P":
                            key = True
                            break
                        # 만약 아랫부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i + 1][j] == "O":
                            if i + 2 < 5:
                                if nowArr[i + 2][j] == "P":
                                    key = True
                                    break
                    # 바로 오른쪽 부분에 사람이 존재하면 break
                    if j + 1 < 5:
                        if nowArr[i][j + 1] == "P":
                            key = True
                            break
                        # 만약 오른쪽 부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i][j + 1] == "O":
                            if j + 2 < 5:
                                if nowArr[i][j + 2] == "P":
                                    key = True
                                    break
                    # 우측 아래 부분입니다.
                    if i + 1 < 5 and j + 1 < 5:
                        # 만약 우측 아래가 사람이고, 오른 쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j + 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j + 1] == "O"):
                            key = True
                            break

                    # 좌측 아래부분입니다.
                    if i + 1 < 5 and j - 1 >= 0:
                        # 만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j - 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j - 1] == "O"):
                            key = True
                            break

        # 위의 for문동안 key가 True로 변경되었다면 거리두가기 지켜지지 않은것 이므로 0을 answer에 추가
        if key:
            answer.append(0)
        else:
            # key가 false로 끝났다면 거리두기가 지켜졌으므로 1 추가
            answer.append(1)
    return answer

# print(solution_other(places_1))

from collections import deque

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]

def BFS(place, x, y):
    visited = [[0 for y in range(5)] for x in range(5)]
    deq = deque()
    deq.append([x, y, 0])
    visited[x][y] = 1

    while deq:
        now = deq.popleft()

        if 1 <= now[2] <= 2 and place[now[0]][now[1]] == 'P':
            return False

        if 3 <= now[2]:
            break

        for move in range(4):
            nxt = [0, 0, 0]
            nxt[0] = now[0] + move_x[move]
            nxt[1] = now[1] + move_y[move]
            nxt[2] = now[2] + 1

            if 0 <= nxt[0] < 5 and 0 <= nxt[1] < 5:
                if place[nxt[0]][nxt[1]] != 'X' and visited[nxt[0]][nxt[1]] == 0:
                    deq.append(nxt)
                    visited[nxt[0]][nxt[1]] = 1

    return True

def solution_best(places):
    answer = []

    for place in places:
        false_place = True
        for x in range(len(place)):
            for y in range(len(place[0])):
                if place[x][y] == 'P':
                    if BFS(place, x, y) == False:
                        false_place = False
                        break
            if false_place == False:
                break

        if false_place == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution_best(places_1))