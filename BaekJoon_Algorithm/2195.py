# 2195. 문자열 복사

"""
I didn't solve this problem by myself. I think this is a little hard version of simple implementation.
The key of this problem is finding the longest overlapping words between P and S.
See it again.
"""
# 1. My Solution
S = input()
target_P = input()
index_p = 0
answer = 0

while index_p < len(target_P):
    index_s, overlaps, max_value = 0, 0, 0
    for index_s in range(len(S)):
        if index_p + overlaps >= len(target_P):
            break

        if target_P[index_p + overlaps] == S[index_s]:
            overlaps += 1
            max_value = max(max_value, overlaps)
        else:
            overlaps = 0
    index_p += max_value
    answer += 1

print(answer)

# # 2. Not my Solution(Blog 1)
# import sys
# input = sys.stdin.readline
#
# S = input().strip()
# P = input().strip()
# index_p = 0
# ans = 0
#
# while index_p < len(P):
#     max_value, temp, index_s = 0, 0, 0
#     while index_s < len(S) and index_p + temp < len(P):
#         if P[index_p + temp] == S[index_s]:
#             temp += 1
#             max_value = max(max_value, temp)
#         else:
#             temp = 0
#         index_s += 1
#     index_p += max_value
#     ans += 1
#
# print(ans)

# 3. Not my Solution(Blog 2)
fst = input()
scd = input()
rst = 0
start = 0 #문자 시작 인덱싱
end = 0 #끝 인덱싱
while True:
    if start == len(scd): #scd문자열 모두 탐색했다면
        break
    for i in range(len(fst) - (end - start)): #길이만큼의 문자열 있는지
        if fst[i:i + (end - start) + 1] == scd[start:end + 1]: #있다면 길이 1을 늘려서 한번더 탐색
            end += 1
            break
    else: #없다면 결과값, 문자 인덱싱 갱신
        rst += 1
        end -= 1
        start = end + 1
        end = start
print(rst)
"""
xy0z
zzz0yyy0xxx
=>
10

"""