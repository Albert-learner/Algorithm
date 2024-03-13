# 1543. 문서 검색

"""
I solve this problem by myself. I use Python's re module for solving regular expression.
findall function can find non-overlap searching expression.
"""
# 1. My Solution
import re
document = input()
search_word = input()

print(len(re.findall(search_word, document)))

# 2. Not my Solution
word = input()
small = input()
sp_word = word.split(small)

print(len(sp_word) - 1)
"""
ababababa
aba
=>
2
==============
a a a a a
a a
=>
2
==============
ababababa
ababa
=>
1
==============
aaaaaaa
aa
=>
3
"""