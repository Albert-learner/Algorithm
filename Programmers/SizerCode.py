# 19.  시저 암호

def solution(s, n):
    answer = ''

    for char in s:
        if char.isalpha():
            if 65 <= ord(char) <= 90:
                if ord(char) + n > 90:
                    answer += chr(ord(char) - 26 + n)
                else:
                    answer += chr(ord(char) + n)
            else:
                if ord(char) + n > 122:
                    answer += chr(ord(char) - 26 + n)
                else:
                    answer += chr(ord(char) + n)
        else:
            answer += ' '
    return answer

s_1 = 'AB'
s_2 = 'z'
s_3 = 'a B z'

n_1 = 1
n_2 = 1
n_3 = 4

print(solution(s_1, n_1))
print(solution(s_2, n_2))
print(solution(s_3, n_3))

def solution_best(s, n):
    answer = ''
    str = list(s)
    for i in range(len(str)):
        if str[i].isupper():
            str[i] = chr((ord(str[i]) - ord('A') + n) % 26 + ord('A'))
        elif str[i].islower():
            str[i] = chr((ord(str[i]) - ord('a') + n) % 26 + ord('a'))

    answer = ''.join(str)
    return answer

print(solution_best(s_1, n_1))
print(solution_best(s_2, n_2))
print(solution_best(s_3, n_3))
# 틀린 풀이
def solution_error(s, n):
    answer = ''

    # string을 ascii로 바꾼 리스트
    str_ascii_lst = [ord(i) for i in s]
    # print(str_ascii_lst)

    for idx, cost in enumerate(str_ascii_lst):
        if cost == 32:
            str_ascii_lst[idx] -= 4
        str_ascii_lst[idx] += n

    # print(str_ascii_lst)
    for i in str_ascii_lst:
        idx = str_ascii_lst.index(i)
        if 90 < i and i < 97:
            rest = i - 90
            str_ascii_lst[idx] = 64 + rest
        elif 122 < i:
            rest = i - 122
            str_ascii_lst[idx] = 96 + rest

    answer = ''.join(chr(i) for i in str_ascii_lst)
    return answer