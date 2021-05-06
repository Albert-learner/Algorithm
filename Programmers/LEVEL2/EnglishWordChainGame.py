# 29. 영어 끝말잇기

'''조금만 더 생각해서 풀지'''
def solution(n, words):
    answer = [0, 0]

    count = 1
    for idx in range(1, len(words)):
        word = words[idx]
        count %= n
        if (word in words[:idx]) or (words[idx - 1][-1] != word[0]):
            answer = [count + 1, 1 + idx // n]
            break
        count += 1

    return answer

n_1 = 3
n_2 = 5
n_3 = 2

words_1 = ["tank", "kick", "know", "wheel", "land", "dream",
           "mother", "robot", "tank"]
words_2 = ["hello", "observe", "effect", "take", "either",
           "recognize", "encourage", "ensure", "establish", "hang",
           "gather", "refer", "reference", "estimate", "executive"]
words_3 = ["hello", "one", "even", "never", "now", "world", "draw"]

# print(solution(n_1, words_1))
# print(solution(n_2, words_2))
# print(solution(n_3, words_3))

'''아예 잘못 생각한 듯'''
def solution_mine(n, words):
    answer = []

    word_cnts = {words[0]: 1}
    check = [words[0]]
    for i in range(1, len(words)):
        check.append(words[i])

        if check[0][-1] == check[1][0]:
            word_cnts[words[i]] = word_cnts.get(words[i], 0) + 1
            for value in word_cnts.values():
                if value == 2:
                    answer = [(i + 1) % n + n, (i + 1) // n]
            check.pop(0)
        else:
            answer = [len(words) % n, len(words) // n]
            break

    if not answer:
        answer = [0, 0]
    return answer

# print(solution_mine(n_1, words_1))
# print(solution_mine(n_2, words_2))
# print(solution_mine(n_3, words_3))

def solution_best(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]:
            return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]

print(solution_best(n_1, words_1))
print(solution_best(n_2, words_2))
print(solution_best(n_3, words_3))