# 8. 스티커 모으기(2)

'''
점화식을 이용한 풀이
맨 앞 스티커 떼는 경우와 아닌 경우로 나눠서 푼다
'''
def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]

    # 맨 앞 스티커 떼는 경우
    table = [0 for _ in range(len(sticker))]
    table[0] = sticker[0]
    table[1] = table[0]
    for i in range(2, len(sticker) - 1):
        table[i] = max(table[i - 1], table[i - 2] + sticker[i])
    value = max(table)

    # 맨 앞 스티커 떼지 않는 경우
    table1 = [0 for _ in range(len(sticker))]
    table1[0] = 0
    table1[1] =  sticker[1]
    for i in range(2, len(sticker)):
        table1[i] = max(table1[i - 1], table1[i - 2] + sticker[i])

    answer = max(value, max(table1))
    return answer

sticker_1 = [14, 6, 5, 11, 3, 9, 2, 10]
sticker_2 = [1, 3, 2, 5, 4]

print(solution(sticker_1))
print(solution(sticker_2))

'''
내 풀이 너무 쉽게 2개씩 건너뛰어서만 생각했음, 오히려 처음 점화식 풀이가
답에 더 근접함.
'''
def solution_error(sticker):
    answer = 0

    cases = []
    for i in range(len(sticker) % 3):
        case = []
        for cost in sticker[i::2]:
            case.append(cost)
        cases.append(sum(case))
    answer = max(cases)
    return answer

def solution_other(sticker):
    n = len(sticker)

    # 맨 처음 스티커를 떼었을 때
    dp = [0] * n
    dp[0] = sticker[0]
    if n == 1:
        return max(dp)

    dp[1] = sticker[1]
    if n == 2:
        return max(dp)

    dp[2] = max(sticker[1], sticker[0] + sticker[2])
    if n == 3:
        return max(dp)

    for i in range(3, n - 1):
        dp[i] = max(dp[i - 3] + sticker[i], dp[i - 2] + sticker[i], dp[i - 1])

    # 맨 처음 스티커를 떼지 않을 때
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])

    for i in range(3, n):
        dp2[i] = max(dp2[i - 3] + sticker[i], dp2[i - 2] + sticker[i], dp2[i - 1])

    return max(max(dp), max(dp2))

# print(solution_other(sticker_1))
# print(solution_other(sticker_2))




