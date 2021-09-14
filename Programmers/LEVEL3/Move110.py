# 11. 110 옮기기

'''
사전 순으로 앞으로 배열 -> 문자열 내에서 모든 '110' 다 뽑아내기
110 의 경우는 이미 사전순서로 배열이 잘 이루어진 문자열이므로
0을 만나면 그 0의 뒤에
1을 만나면 그 1의 앞에
위치시켜준다.
'''
def move(string):
    p = list('110')
    size_s = len(string)

    count, stack = 0, []
    for i in range(size_s):
        stack.append(string[i])
        if stack[-3:] == p:
            stack.pop()
            stack.pop()
            stack.pop()

    size_stack = len(stack)
    count = int((size_s - size_stack) / 3)

    for i in range(size_stack + 1):
        temp = (stack[i:i + 3] * 3)[:3]
        if temp > p: break

    new_s = stack[:i] + p * count + stack[i:]

    return ''.join(new_s)

def solution(s):
    answer = [move(string) for string in s]

    return answer

s_1 = ["1110","100111100","0111111010"]

print(solution(s_1))

def solution_other(s):
    answer = []

    def extract(s):
        count, stack = 0, []
        for _s in s:
            if _s == '0' and stack[-2:] == ['1', '1']:
                stack.pop()
                stack.pop()
                count += 1
            else:
                stack.append(_s)

        return ''.join(stack), count

    def rearrange(s):
        for i in range(-1, -len(s) - 1, -1):
            pointer = len(s) + (i + 1)
            if s[i] == '0':
                return s[:pointer] + '110' + s[pointer:]

        return '110' + s

    for _s in s:
        _s, count = extract(_s)
        for _ in range(count):
            _s = rearrange(_s)
        answer.append(_s)
    return answer

# print(solution_other(s_1))

from collections import deque
def solution_best(s):
    answer = []

    for string in s:
        count, stack = 0, []
        for ch in string:
            if ch == '0':
                if stack[-2:] == ['1', '1']:
                    count += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        if count == 0:
            answer.append(string)
        else:
            final = deque()

            while stack:
                if stack[-1] == '1':
                    final.appendleft(stack.pop())
                elif stack[-1] == '0':
                    break

            while count > 0:
                final.appendleft('0')
                final.appendleft('1')
                final.appendleft('1')
                count -= 1

            while stack:
                final.appendleft(stack.pop())

            answer.append(''.join(final))
    return answer

# print(solution_best(s_1))