# 1. 단어 퍼즐

def solution(strs, t):
    answer = 0

    n = len(t)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = float('inf')
        for k in range(1, 6):
            if i - k < 0:
                s = 0
            else:
                s = i - k

            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)

    if dp[-1] == float('inf'):
        answer = -1
    else:
        answer = dp[-1]

    return answer

strs_1 = ["ba","na","n","a"]
strs_2 = ["app","ap","p","l","e","ple","pp"]
strs_3 = ["ba","an","nan","ban","n"]
strs_4 = ["ab", "na", "n", "a", "bn"]
strs_5 = ["H", "e", "o", "He", "ll"]
strs_6 = ["Py", "t", "h", "tho", "on", "thon"]

t_1 = "banana"
t_2 = "apple"
t_3 = "banana"
t_4 = "nabnabn"
t_5 = "Hello"
t_6 = "Python"

print(solution(strs_1, t_1))
print(solution(strs_2, t_2))
print(solution(strs_3, t_3))
print(solution(strs_4, t_4))
print(solution(strs_5, t_5))
print(solution(strs_6, t_6))

print()
import math
def solution_other(strs, t):
    answer = 0

    default = math.inf
    dp = [default for i in range(len(t) + 1)]
    dp[0] = 0

    for i in range(1, len(t) + 1):
        j = i - 5 if i > 5 else 0
        while j < i:
            if dp[j] + 1 < dp[i] and t[j:i] in strs:
                dp[i] = dp[j] + 1
            j += 1

    answer = dp[-1] if dp[-1] != default else -1
    return answer

strs_1 = ["ba","na","n","a"]
strs_2 = ["app","ap","p","l","e","ple","pp"]
strs_3 = ["ba","an","nan","ban","n"]
strs_4 = ["ab", "na", "n", "a", "bn"]
strs_5 = ["H", "e", "o", "He", "ll"]
strs_6 = ["Py", "t", "h", "tho", "on", "thon"]

t_1 = "banana"
t_2 = "apple"
t_3 = "banana"
t_4 = "nabnabn"
t_5 = "Hello"
t_6 = "Python"

print(solution_other(strs_1, t_1))
print(solution_other(strs_2, t_2))
print(solution_other(strs_3, t_3))
print(solution_other(strs_4, t_4))
print(solution_other(strs_5, t_5))
print(solution_other(strs_6, t_6))