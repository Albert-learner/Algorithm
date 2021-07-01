# 48. 방문 길이

def solution(dirs):
    answer = 0

    move = {'R' : (1, 0), 'L' : (-1, 0), 'D' : (0, -1), 'U' : (0, 1)}
    visited = set()
    current_x , current_y = 0, 0
    for dir in dirs:
        move_x, move_y = current_x + move[dir][0], current_y + move[dir][1]
        if -5 <= move_x <= 5 and -5 <= move_y <= 5:
            visited.add((current_x, current_y, move_x, move_y))
            visited.add((move_x, move_y, current_x, current_y))
            current_x, current_y = move_x, move_y

    answer = len(visited) // 2
    return answer

dirs_1 = "ULURRDLLU"
dirs_2 = "LULLLLLLU"

print(solution(dirs_1))
print(solution(dirs_2))

'''
25점
현재 좌표를 나타내는 currents list에
지났던 경로가 있는지 없는지 저장하는 visited list로
각 문자에 맞게 동,서,남,북 값에 맞게 currents list의 값을 초기화해준다
만약에 -5 <= x <= 5, -5 <= y <= 5 사이에 있으면 위 같이 풀고
아니면 그냥 넘어가면 됨
----------------------------------------------------------------
가는 길만 표시하면 될 것 같았는데 오는 길이 안 겹칠 수도 있겠네
그래서 set자료형을 사용해서 풀어야
'''
def solution_mine(dirs):
    answer = []

    currents = [0, 0]
    visited = []
    for dir in dirs:
        x, y, = currents[0], currents[1]
        if -5 <= x and x <= 5 and -5 <= y and y <= 5:
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'D':
                y -= 1
            elif dir == 'U':
                y += 1

            if [x, y] not in visited:
                visited.append([x, y])
                answer += 1
                currents[0], currents[1] = x, y
            else:
                answer += 1
                break
        else:
            continue

    return answer

def solution_other(dirs):
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    d = {"U": 0, "L": 1, "D": 2, "R": 3}

    visited = set()
    answer = 0
    x, y = 0, 0
    for dir in dirs:
        i = d[dir]
        nx, ny = x + dxs[i], y + dys[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))  # 길은 '양방향' 임을 빼먹으면 안됨!
            answer += 1
        x, y = nx, ny

    return answer

print(solution_other(dirs_1))
print(solution_other(dirs_2))