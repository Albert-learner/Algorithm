# 코드업 100제 마지막 문제

"""
I almost solve this problem by myself. But I miss after finding the target coordinate.
The easiest way is applying infinity loop for finding target coordinate.
And make some exceptions.
See it again.
"""
miro_box = [list(map(int, input().split())) for _ in range(10)]

start_x, start_y = 1, 1
while True:
    if miro_box[start_x][start_y] == 0:
        miro_box[start_x][start_y] = 9
    elif miro_box[start_x][start_y] == 2:
        miro_box[start_x][start_y] = 9
        break

    if miro_box[start_x][start_y + 1] == 1 and miro_box[start_x + 1][start_y] == 1:
        break

    if miro_box[start_x][start_y + 1] != 1:
        start_y += 1
    elif miro_box[start_x + 1][start_y] != 1:
        start_x += 1

for row in range(len(miro_box)):
    for col in range(len(miro_box[0])):
        print(miro_box[row][col], end=' ')
    print()