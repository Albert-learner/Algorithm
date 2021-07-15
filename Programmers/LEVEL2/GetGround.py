# 53. 땅따먹기

def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[len(land) - 1])
    return answer

land_1 = [[1, 2, 3, 5],
          [5, 6, 7, 8],
          [4, 3, 2, 1]
          ]

print(solution(land_1))

def solution_other(land):
    for i in range(len(land) - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])

    return max(land[-1])

land_1 = [[1, 2, 3, 5],
          [5, 6, 7, 8],
          [4, 3, 2, 1]
          ]
print(solution_other(land_1))