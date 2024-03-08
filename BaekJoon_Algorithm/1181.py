# 1181. 단어 정렬

"""
I almost solve this problem by myself. But I miss a little point that Python sort function can sorting with multiple arguments.
"""
# 1. My Solution
N = int(input())
words_lst = list(set([input() for _ in range(N)]))
# print(sorted(words_lst, key=lambda x: (len(x), x)))
for word in sorted(words_lst, key=lambda x: (len(x), x)):
    print(word)

# 2. Not my Solution



"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
=>
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""