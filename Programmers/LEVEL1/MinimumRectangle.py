# 50. 최소 직사각형

def solution(sizes):
    answer = 0

    width = list(zip(*sizes))[0]
    height = list(zip(*sizes))[1]
    w_lst, h_lst = [], []
    if max(width) < max(height):
        for w, h in sizes:
            if h < w:
                w, h = h, w
            w_lst.append(w)
            h_lst.append(h)
    else:
        for w, h in sizes:
            if w < h:
                w, h = h, w
            w_lst.append(w)
            h_lst.append(h)


    answer = max(w_lst) * max(h_lst)
    return answer

sizes_1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes_2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes_3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes_1))
print(solution(sizes_2))
print(solution(sizes_3))

def solution_best(sizes):
    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)

    return answer

# print(solution_best(sizes_1))
# print(solution_best(sizes_2))
# print(solution_best(sizes_3))