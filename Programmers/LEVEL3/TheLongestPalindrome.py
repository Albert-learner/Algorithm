# 30. 가장 긴 펠린드롬

def isPalindrome(st):
    if st == st[::-1]:
        return True
    return False

def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]):
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
    return answer

s_1 = 'abcdcba'
s_2 = 'abacde'

print(solution(s_1))
print(solution(s_2))