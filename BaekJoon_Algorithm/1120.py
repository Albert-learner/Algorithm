# 1120. 문자열

"""
I didn't solve this problem by myself. I'm trying to find the rules in two strings.
But this requires finding all rules in two strings(Brute-Force Algorithm).
"""
# 1. My Solution
strs_lst = input().split()
diff_lst = []
A, B = strs_lst

for j in range(len(B) - len(A) + 1):
    diff_cnt = 0
    for i in range(len(A)):
        if A[i] != B[i + j]:
            diff_cnt += 1

    diff_lst.append(diff_cnt)

print(min(diff_lst))

# # 2. Not my Solution
# A, B = input().split()
#
# answer = []
# for i in range(len(B) - len(A) + 1):
#     count = 0
#     for j in range(len(A)):
#         if A[j] != B[i + j]:
#             count += 1
#     answer.append(count)
#
# print(min(answer))
"""
adaabc aababbc
=>
2
==================
hello xello
=>
1
==================
koder topcoder
=>
1
==================
abc topabcoder
=>
0
==================
giorgi igroig
=>
6
"""