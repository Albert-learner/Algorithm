# 28. 비밀 지도

def solution(n, arr1, arr2):
    answer = []

    # 지도 1 2진수 문자열로 바꾼 리스트 ... 9 -> '0b1001'
    bi_map1_lst = [bin(i) for i in arr1]

    # 지도 1 2진수 문자열 정리한 리스트 ... '0b1001' -> '1001'
    map1_lst = []

    # 지도 2 2진수 문자열로 바꾼 리스트(지도 1과 같음)
    bi_map2_lst = [bin(i) for i in arr2]

    # 지도 2 2진수 문자열 정리한 리스트(지도 1과 같음)
    map2_lst = []

    # '0b1001' -> '1001'
    for one in bi_map1_lst:
        one = one[2:]
        map1_lst.append(one)

    for one in bi_map2_lst:
        one = one[2:]
        map2_lst.append(one)

    # '1001' -> '01001' or '01001' -> '1001'
    for i in range(len(map1_lst)):
        if len(map1_lst[i]) < n:
            map1_lst[i] = (n - len(map1_lst[i])) * '0' + map1_lst[i]

    for i in range(len(map2_lst)):
        if len(map2_lst[i]) < n:
            map2_lst[i] = (n - len(map2_lst[i])) * '0' + map2_lst[i]

    for line1, line2 in zip(map1_lst, map2_lst):
        # 줄 별 문자열 저장 ... '#####'
        line_str = ''
        for sq1, sq2 in zip(line1, line2):
            if sq1 == '1' or sq2 == '1':
                line_str += '#'
            elif sq1 == '0' and sq2 == '0':
                line_str += ' '
        answer.append(line_str)
    return answer

n_1 = 5
arr1_1 = [9, 20, 28, 18, 11]
arr2_1 = [30, 1, 21, 17, 28]

n_2 = 6
arr1_2 = [46, 33, 33, 22, 31, 50]
arr2_2 = [27, 56, 19, 14, 14, 10]

print(solution(n_1, arr1_1, arr2_1))
print(solution(n_2, arr1_2, arr2_2))
print()

def solution_best(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        a12 = bin(i | j)[2:]
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer

print(solution_best(n_1, arr1_1, arr2_1))
print(solution_best(n_2, arr1_2, arr2_2))
