# 13. N으로 표현

def solution(N, number):
    answer = -1

    possible_set = [0, [N]]
    if N == number:
        return 1

    for i in range(2, 9):
        case_set = []
        basic_num = int(str(N) * i)
        case_set.append(basic_num)
        for i_half in range(1, i // 2 + 1):
            for x in possible_set[i_half]:
                for y in possible_set[i - i_half]:
                    case_set.append(x + y)
                    case_set.append(x - y)
                    case_set.append(y - x)
                    case_set.append(x * y)

                    if y != 0:
                        case_set.append(x / y)
                    if x != 0:
                        case_set.append(y / x)

            if number in case_set:
                return i
            possible_set.append(case_set)

    return answer

N_1 = 5
N_2 = 2

number_1 = 12
number_2 = 11

print(solution(N_1, number_1))
print(solution(N_2, number_2))

answer = -1

def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            # print(s)
            answer = pos
        return

    nn = 0
    for i in range(8):
        nn = nn * 10 + n
        DFS(n, pos + 1 + i, num + nn, number, s + '+')
        DFS(n, pos + 1 + i, num - nn, number, s + '-')
        DFS(n, pos + 1 + i, num * nn, number, s + '*')
        DFS(n, pos + 1 + i, num / nn, number, s + '/')

def solution_other(N, number):
    DFS(N, 0, 0, number, '')

    return answer

# print(solution_other(N_1, number_1))
# print(solution_other(N_2, number_2))

def solution_best(N, number):
    answer = -1

    DP = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            answer = i
            break

        DP.append(numbers)
    return answer

print(solution_best(N_1, number_1))
print(solution_best(N_2, number_2))