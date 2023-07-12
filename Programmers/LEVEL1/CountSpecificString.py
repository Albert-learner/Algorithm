# Restart 29. 문자열이 몇 번 등장하는지 세기

def solution(myString, pat):
    answer = 0

    for idx, chr in enumerate(myString):
        if myString[idx:].startswith(pat):
            answer += 1

    return answer

myString_1 = 'banana'
myString_2 = 'aaaa'

pat_1 = 'ana'
pat_2 = 'aa'

print(solution(myString_1, pat_1))
print(solution(myString_2, pat_2))

def solution_best(myString, pat):
    answer = sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))

    return answer

print(solution_best(myString_1, pat_1))
print(solution_best(myString_2, pat_2))