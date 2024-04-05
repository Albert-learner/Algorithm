# 옹알이2

"""
I didn't solve this problem by myself. The key of this problem is a simple implementation.
Think problem simple, not complicated.
See it again.
"""
def solution(babbling):
    answer = 0

    possibles = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        for possible in possibles:
            if possible * 2 not in babble:
                babble = babble.replace(possible, ' ')

        if babble.isspace():
            answer += 1

    return answer

babbling_1 = ["aya", "yee", "u", "maa"]
babbling_2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling_1))
print(solution(babbling_2))