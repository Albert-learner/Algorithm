# Restart 39. 바탕화면 정리

def solution(wallpaper):
    answer = []

    board = [[elem for elem in row] for row in wallpaper]
    board_row, board_col = len(board), len(board[0])

    files_loc_lst = []
    for row_idx in range(board_row):
        for col_idx in range(board_col):
            if board[row_idx][col_idx] == '#':
                files_loc_lst.append((row_idx, col_idx))

    row_lst, col_lst = [], []
    for row, col in files_loc_lst:
        row_lst.append(row)
        col_lst.append(col)

    row_min, row_max = min(row_lst), max(row_lst) + 1
    col_min, col_max = min(col_lst), max(col_lst) + 1
    answer = [row_min, col_min, row_max, col_max]
    return answer

wallpaper_1 = [".#...", "..#..", "...#."]
wallpaper_2 = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
wallpaper_3 = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
wallpaper_4 = ["..", "#."]

print(solution(wallpaper_1))
print(solution(wallpaper_2))
print(solution(wallpaper_3))
print(solution(wallpaper_4))