# 21. 올바른 괄호

def solution(s):
    answer = True

    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                answer = False
                return answer
            else:
                stack.pop()

    answer = len(stack) == 0
    return answer

s_1 = '()()'
s_2 = '(())()'

print(solution(s_1))
print(solution(s_2))

'''())( 때문에 이렇게 풀면 안 됨'''
def solution_mine(s):
    answer = True

    left_buckets = s.count('(')
    right_buckets = s.count(')')
    if left_buckets != right_buckets:
        answer = False
        return answer
    else:
        if s[0] == ')':
            answer = False
            return answer
        else:
            stack = [s[0]]
            for char in range(1, len(s)):
                if char == '(':
                    stack.append(char)
                else:
                    if len(stack) != 0:
                        stack.pop(0)

    return answer

# print(solution_mine(s_1))
# print(solution_mine(s_2))