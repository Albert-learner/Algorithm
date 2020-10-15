# 7. K번째 수

def solution(array, commands):
    answer = []

    # commands 리스트 돌면서 조건에 맞게 찾기
    for i in commands:
        arr_slice = array[i[0] - 1:i[1]]
        # print(arr_slice)

        arr_slice.sort()
        # print(arr_slice)

        answer.append(arr_slice[i[2] - 1])
    return answer

array_1 = [1, 5, 2, 6, 3, 7, 4]
commands_1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array_1, commands_1))

def solution_best(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))

print(solution_best(array_1, commands_1))