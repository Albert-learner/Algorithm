# 1063. 킹

"""
I didn't solve this problem by myself. I miss two key points.
First is the starting position of king and stone(1, 1).
Last one is the overlapped of king and stone.
See this again.
"""
# 1.My Solution(practice)
king_pos_str, stone_pos_str, N = input().split()
king_moving_poses = [input() for _ in range(int(N))]

king_moves_dict = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
                   'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1),
                   'LB': (-1, -1)}

king_pos = [int(ord(king_pos_str[0])) - int(ord('A')) + 1, int(king_pos_str[1])]
stone_pos = [int(ord(stone_pos_str[0])) - int(ord('A')) + 1, int(stone_pos_str[1])]

for king_move in king_moving_poses:
    move_r, move_c = king_moves_dict[king_move]
    move_king_x, move_king_y = king_pos[0] + move_r, king_pos[1] + move_c
    if move_king_x in range(1, 9) and move_king_y in range(1, 9):
        if move_king_x == stone_pos[0] and move_king_y == stone_pos[1]:
            move_stone_x, move_stone_y = stone_pos[0] + move_r, stone_pos[1] + move_c
            if move_stone_x in range(1, 9) and move_stone_y in range(1, 9):
                king_pos = [move_king_x, move_king_y]
                stone_pos = [move_stone_x, move_stone_y]
        else:
            king_pos = [move_king_x, move_king_y]

print(chr(king_pos[0] + ord('A') - 1) + str(king_pos[1]))
print(chr(stone_pos[0] + ord('A') - 1) + str(stone_pos[1]))

# 1. My Solution

# A1, A2(string + string)
king_pos_str, stone_pos_str, move_cnts_str = input().split()
move_cnts = int(move_cnts_str)
king_moving_poses = [input() for _ in range(move_cnts)]

king_moves_dict = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
                   'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
                   }

king_pos = [int(ord(king_pos_str[0])) - int(ord('A')) + 1, int(king_pos_str[1])]
stone_pos = [int(ord(stone_pos_str[0])) - int(ord('A')) + 1, int(stone_pos_str[1])]

for king_move in king_moving_poses:
    move_r, move_c = king_moves_dict[king_move]
    moved_king_x, moved_king_y = king_pos[0] + move_r, king_pos[1] + move_c
    if moved_king_x in range(1, 9) and moved_king_y in range(1, 9):
        if moved_king_x == stone_pos[0] and moved_king_y == stone_pos[1]:
            if moved_king_x == stone_pos[0] and moved_king_y == stone_pos[1]:
                moved_stone_x = stone_pos[0] + move_r
                moved_stone_y = stone_pos[1] + move_c
                if moved_stone_x in range(1, 9) and moved_stone_y in range(1, 9):
                    king_pos = [moved_king_x, moved_king_y]
                    stone_pos = [moved_stone_x, moved_stone_y]
        else:
            king_pos = [moved_king_x, moved_king_y]

print(chr(king_pos[0] + ord('A') - 1) + str(king_pos[1]))
print(chr(stone_pos[0] + ord('A') - 1) + str(stone_pos[1]))

# 2. Not my Solution
king, stone, N = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))

# 이때 k와 s는 [1,1] [8,8]

# 딕셔너리 (이동 타입에 따라 dx와 dy 설정)
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1],
        'LB': [-1, -1]}

# 움직이는 횟수 만큼 실행
for _ in range(int(N)):
    m = input()  # 지금 이동

    # 움직였을 경우의 위치 : nx, ny
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]

    # 킹 조건 검사
    if 0 < nx <= 8 and 0 < ny <= 8:
        # 돌 위에 얹히는가?
        if nx == s[0] and ny == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            # 돌 조건 검사
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]  # 킹 이동
                s = [sx, sy]  # 돌 이동
        else:
            k = [nx, ny]  # 킹만 이동
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')



"""
A1 A2 5
B
L
LB
RB
LT
=>
A1
A2
===============
A1 H8 1
T
=>
A2
H8
===============
A1 A2 1
T
=>
A2
A3
===============
A1 A2 2
T
R
=>
B2
A3
===============
A8 B7 18
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
=>
G2
H1
==================
C1 B1 3
L
T
LB
=>
B2
A1
"""