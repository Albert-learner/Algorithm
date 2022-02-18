# 26. 기둥과 보 설치

def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:
            if y != 0 and (x, y - 1, COL) not in result and \
                    (x - 1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else:
            if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and \
                    not ((x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                return True
    return False

def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)

    answer = map(list, result)
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer

n_1 = 5
n_2 = 5

build_frame_1 = [[1, 0, 0, 1],
                 [1, 1, 1, 1],
                 [2, 1, 0, 1],
                 [2, 2, 1, 1],
                 [5, 0, 0, 1],
                 [5, 1, 0, 1],
                 [4, 2, 1, 1],
                 [3, 2, 1, 1]
                 ]
build_frame_2 = [[0, 0, 0, 1],
                 [2, 0, 0, 1],
                 [4, 0, 0, 1],
                 [0, 1, 1, 1],
                 [1, 1, 1, 1],
                 [2, 1, 1, 1],
                 [3, 1, 1, 1],
                 [2, 0, 0, 0],
                 [1, 1, 1, 0],
                 [2, 2, 0, 1]
                 ]

print(solution(n_1, build_frame_1))
print(solution(n_2, build_frame_2))

def check(ans):
    for x, y, what in ans:
        # 기둥
        # 1. 바닥 위에 있어야댐
        # 2. 보의 한쪽 끝 부분 위에 있어야댐
        # 3. 다른 기둥 위에 있어야댐
        if what == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        # 보
        # 1. 한쪽 끝 부분이 기둥 위에 있어야댐
        # 2. 양쪽 끝 부분이 다른 보와 동시에 연결
        elif what == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution_other(n, build_frame):
    answer = []

    for f in build_frame:
        x, y, what, how = f

        if how == 1:  # 설치
            answer.append([x, y, what])
            if check(answer) is False:
                answer.remove([x, y, what])
        else:  # 삭제
            answer.remove([x, y, what])
            if check(answer) is False:
                answer.append([x, y, what])

    answer.sort()
    return answer

print(solution_other(n_1, build_frame_1))
print(solution_other(n_2, build_frame_2))