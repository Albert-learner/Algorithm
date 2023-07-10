# Restart 28. 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

'''
Not solve this problem by myself.
So see this again
'''
def solution(myString, pat):
    answer = myString[:len(myString) - myString[::-1].index(pat[::-1])]
    # print(myString[:len(myString)])
    # print(myString[::-1])
    # print(myString[::-1].index(pat[::-1]))
    # print(myString[myString[::-1].index(pat[::-1])])
    # print(myString[:len(myString) - myString[::-1].index(pat[::-1])])

    return answer

myString_1 = "AbCdEFG"
myString_2 = "AAAAaaaa"

pat_1 = "dE"
pat_2 = "a"

print(solution(myString_1, pat_1))
print(solution(myString_2, pat_2))

def solution_other(myString, pat):
    answer = myString[::-1][myString[::-1].index(pat[::-1]):][::-1]

    return answer

# print(solution_other(myString_1, pat_1))
# print(solution_other(myString_2, pat_2))

solution_best = lambda x, y:x[:x.rindex(y) + len(y)]
# print(solution_best(myString_1, pat_1))
# print(solution_best(myString_2, pat_2))