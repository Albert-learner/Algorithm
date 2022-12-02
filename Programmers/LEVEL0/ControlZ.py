# Restart 14. 컨트롤 제트

# My Solution
def solution(s):
    answer = 0

    s_split = s.split()
    stack = []
    for str_s in s_split:
        if str_s != 'Z':
            stack.append(int(str_s))
        else:
            stack.pop()

    answer = sum(stack)
    return answer

