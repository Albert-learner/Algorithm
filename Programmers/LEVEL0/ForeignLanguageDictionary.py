# Restart 9. 외계어 사전

# My Solution
from itertools import permutations
def solution(spell, dic):
    answer = 2

    comb_spell = [''.join(spell_comb) for spell_comb in list(permutations(spell, len(spell)))]

    for word in dic:
        if word in comb_spell:
            answer = 1

    return answer

spell_1 = ["p", "o", "s"]
spell_2 = ["z", "d", "x"]
spell_3 = ["s", "o", "m", "d"]

dic_1 = ["sod", "eocd", "qixm", "adio", "soo"]
dic_2 = ["def", "dww", "dzx", "loveaw"]
dic_3 = ["moos", "dzx", "smm", "sunmmo", "som"]

print(solution(spell_1, dic_1))
print(solution(spell_2, dic_2))
print(solution(spell_3, dic_3))

def solution_other(spell, dic):
    answer = 2

    spell = set(spell)
    for s in dic:
        if not spell - set(s):
            answer = 1
    return answer

print(solution_other(spell_1, dic_1))
print(solution_other())