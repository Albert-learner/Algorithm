# 1544. 사이클 단어

"""
I didn't solve this problem by myself. I catch how to make cycle words not using deque.
But I didn't catch how to discriminate different words. And I learned Python's deque rotate function.
"""
# 1. My Solution
from collections import deque
def cycle_word(w1, w2):
    if len(w1) != len(w2): return w2
    w2 = deque(w2)

    for _ in range(len(w2)):
        w2.rotate(1)
        c_word = "".join(w2)
        if w1 == c_word: return c_word

    return "".join(w2)

N = int(input())
words_lst = [input() for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        if words_lst[i] != words_lst[j]:
            words_lst[j] = cycle_word(words_lst[i], words_lst[j])

print(len(set(words_lst)))

# 2. Not my Solution
from collections import deque

def rotate_word(w1, w2):
    if len(w1) != len(w2): return w2
    w2 = deque(w2)

    for _ in range(len(w2)):
        w2.rotate(1)
        t = "".join(w2)
        if w1 == t: return t

    return "".join(w2)

n = int(input())
l = [input() for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if l[i] != l[j]:
            l[j] = rotate_word(l[i], l[j])

print(len(set(l)))

"""
5
picture
turepic
icturep
word
ordw
=>
2
===============
7
ast
ats
tas
tsa
sat
sta
ttt
=>
3
===============
5
aaaa
aaa
aa
aaaa
aaaaa
=>
4
"""