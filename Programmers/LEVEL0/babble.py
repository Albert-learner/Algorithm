# Restart 27. 옹알이


from itertools import permutations
def solution(babbling):
    answer = 0

    possible_pron = ['aya', 'ye', 'woo', 'ma']
    possible_word = []
    for i in range(1, len(possible_pron) + 1):
        for j in permutations(possible_pron, i):
            possible_word.append(''.join(j))

    for babb in babbling:
        if babb in possible_word:
            answer += 1
    return answer

babbling_1 = ["aya", "yee", "u", "maa", "wyeoo"]
babbling_2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

print(solution(babbling_1))
print(solution(babbling_2))

'''
Using re module
'''
import re
def solution_best(babbling):
    answer = 0

    regex = re.compile('^(aya|ye|woo|ma)+$')
    for babb in babbling:
        if regex.match(babb):
            answer += 1
            
    return answer

print(solution_best(babbling_1))
print(solution_best(babbling_2))