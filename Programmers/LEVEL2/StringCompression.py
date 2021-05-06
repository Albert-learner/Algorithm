# 8. 문자열 압축

# 감을 못 잡겠네...
def solution(s):
    answer = 0

    pattern = []
    result = ''

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tmpStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tmpStr:
                count += 1
            else:
                if count == 1:
                    count = ''
                result += str(count) + tmpStr
                tmpStr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ''
        result += str(count) + tmpStr
        pattern.append(len(result))
        result = ''

    answer = min(pattern)
    return answer

s_1 = "aabbaccc"
s_2 = "ababcdcdababcdcd"
s_3 = "abcabcdede"
s_4 = "abcabcabcabcdededededede"
s_5 = "xababcdcdababcdcd"

# print(solution(s_1))
# print(solution(s_2))
# print(solution(s_3))
# print(solution(s_4))
# print(solution(s_5))

def solution_best(s):
    answer = 0

    LENGTH = len(s)
    STR, COUNT = 0, 1

    # 1 ~ len까지 압축했을 때 길이 값
    pattern = [LENGTH]

    for cut in range(1, LENGTH):
        result = ''
        # string 갯수 단위로 쪼개기
        splited = [s[i:i+cut] for i in range(0, LENGTH, cut)]
        stack = [[splited[0], 1]]

        for unit in splited[1:]:
            # 이전 문자와 다르다면
            if stack[-1][STR] != unit:
                stack.append([unit, 1])
            # 이전 문자와 다르다면
            else:
                stack[-1][COUNT] += 1

        result += ('').join([str(cnt) + w if cnt > 1 else w
                             for w, cnt in stack])
        pattern.append(len(result))

    answer = min(pattern)
    return answer

print(solution_best(s_1))
print(solution_best(s_2))
print(solution_best(s_3))
print(solution_best(s_4))
print(solution_best(s_5))

def solution_other(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)

# print(solution_other(s_1))
# print(solution_other(s_2))
# print(solution_other(s_3))
# print(solution_other(s_4))
# print(solution_other(s_5))