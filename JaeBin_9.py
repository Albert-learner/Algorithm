# 9. 자동 완성

def solution(words):
    words.sort()
    answer = 0

    for i in range(len(words) - 1):
        countA = 0
        countB = 0

        for w in range(len(words[i])):
            try:
                if (words[i][w] != words[i + 1][w]):
                    countA += 1
                    break
            except:
                countA += 1
                break
            countA += 1

        for w in range(len(words[i])):
            try:
                if (words[i][w] != words[i - 1][w]):
                    countB += 1
                    break
            except:
                countB += 1
                break
            countB += 1

        answer += max(countA, countB)

    countA = 0
    for w in range(len(words[-1])):
        try:
            if (words[-1][w] != words[-2][w]):
                countA += 1
                break
        except:
            countA += 1
            break
        countA += 1
    answer += countA

    return answer

words_1 = ['go', 'gone', 'guild']
words_2 = ['abc', 'def', 'ghi', 'jklm']
words_3 = ['word', 'war', 'warrior', 'world']
print(solution(words_1))
print()
print(solution(words_2))
print()
print(solution(words_3))


# 내 풀이
# def solution(words):
#     words.sort()
#     answer = 0
#
#     for word in range(len(words)-1):
#         count_front = 0
#         count_rear = 0
#
#         min_word_length = min(len(words[word]), len(words[word+1]))
#         for char in range(min_word_length):
#             if words[word][char] != words[word + 1][char]:
#                 count_front += 1
#                 break
#             else:
#                 count_front += 1
#         if len(words[word]) > min_word_length:
#             count_front += 1
#
#         min_word_length = min(len(words[word]), len(words[word-1]))
#         for char in range(min_word_length):
#             if words[word][char] != words[word-1][char]:
#                 count_rear += 1
#                 break
#             else:
#                 count_rear += 1
#         if len(words[word]) > min_word_length:
#             count_rear += 1
#
#         answer += max(count_front, count_rear)
#
#     count_front = 0
#     min_word_length = min(len(words[-1]), len(words[-2]))
#     for char in range(min_word_length):
#         if words[-1][char] != words[-2][char]:
#             count_front += 1
#             break
#         else:
#             count_front += 1
#     answer += count_front
#
#     return answer
#
# words_1 = ['go', 'gone', 'guild']
# words_2 = ['abc', 'def', 'ghi', 'jklm']
# words_3 = ['word', 'war', 'warrior', 'world']
# print(solution(words_1))
# print()
# print(solution(words_2))
# print()
# print(solution(words_3))