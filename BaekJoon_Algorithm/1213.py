# 1213. 팰린드롬 만들기

"""
I didn't solve this problem by myself. The key of this problem is sorting and keep Palindrome.
The rule of making Palindrome is that there's no odd counts of character in english name.
"""
# 1. My Solution
from collections import Counter

english_name = input()
check_words = Counter(english_name)
cnts = 0
change_results = ""
mid = ""
for key, value in check_words.items():
    if value % 2 == 1:
        cnts += 1
        mid = key
        if cnts >= 2:
            print("I'm Sorry Hansoo")
            exit()

for key, value in sorted(check_words.items()):
    change_results += key * (value // 2)

print(change_results + mid + change_results[::-1])

# 2. Not my Solution
import collections
import sys

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''
for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        cnt += 1
        mid = k #중간에 들어갈 값으로 저장
        if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함
    result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력


"""
AABB
=>
ABBA
========
AAABB
=>
ABABA
========
ABACABA
=>

========
ABCD
=>
I'm Sorry Hansoo
"""