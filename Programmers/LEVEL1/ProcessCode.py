# Restart 34. 코드 처리하기

'''
I solve this problem by myself, but I don't understand best solution. So check it again.
'''
def solution(code):
    answer = ''

    for code_idx in range(len(code)):
        mode = 0 if code_idx == 0 else mode
        if mode == 0:
            if code[code_idx] != '1':
                if code_idx % 2 == 0:
                    answer += code[code_idx]
            else:
                mode = 1
        elif mode == 1:
            if code[code_idx] != '1':
                if code_idx % 2 == 1:
                    answer += code[code_idx]
            else:
                mode = 0

    if len(answer) == 0:
        answer = 'EMPTY'

    return answer

code_1 = "abc1abc1abc"

# print(solution(code_1))

def solution_best(code):
    answer = ''.join(code.split('1'))[::2] or 'EMPTY'

    # print(code.split('1'))
    # print(''.join(code.split('1'))[::2])
    # print(''.join(code.split('1'))[::2] or 'EMPTY')
    return answer

print(solution_best(code_1))