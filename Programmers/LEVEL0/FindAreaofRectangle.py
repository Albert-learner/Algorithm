# Restart 12. 직사각형 넓이 구하기

def solution(dots):
    dots.sort()
    answer = abs(dots[3][0] - dots[0][0]) * abs(dots[3][1] - dots[0][1])

    return answer

dots_1 = [[1, 1], [2, 1], [2, 2], [1, 2]]
dots_2 = [[-1, -1], [1, 1], [1, -1], [-1, 1]]

print(solution(dots_1))
print(solution(dots_2))

def solution_best(dots):
    answer = (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])

    return answer

print(solution_best(dots_1))
print(solution_best(dots_2))