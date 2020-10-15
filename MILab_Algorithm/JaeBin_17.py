# 17. 프로그래머스 - 불량 사용자

answer_lst = []
def compare(ban_str, user_str):
    if len(ban_str) != len(user_str):
        return False
    else:
        for i in range(len(ban_str)):
            if ban_str[i] == user_str[i] or ban_str[i] == '*':
                continue
            else:
                return False
        return True

def DFS(idx, chk_set, cand_lst):
    if idx == len(cand_lst):
        if len(chk_set) == len(cand_lst):
            answer_set = set(answer_lst)
            for i in range(len(answer_set)):
                if i == chk_set:
                    return


def solution(user_id, banned_id):
    # 변수 선언
    answer = 0
    candidates = []

    # banned_id 개수만큼 비교
    for word in range(len(banned_id)):
        # banned_id 하나당 가능한 단어 저장 list
        possible = []

        # user_id 개수만큼 비교
        for w in range(len(user_id)):
            if compare(banned_id[word], user_id[w]):
                possible.append(user_id[w])
        candidates.append(possible)

    chk = set()
    DFS(0, chk, candidates)
    return answer

user_id_1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_1 = ["fr*d*", "abc1**"]

user_id_2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_2 = ["*rodo", "*rodo", "******"]

user_id_3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_3 = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id_1, banned_id_1))
print()
print(solution(user_id_2, banned_id_2))
print()
print(solution(user_id_3, banned_id_3))

'''
다른 사람들의 풀이를 참조하여 풀었습니다.
'''
# # 특정 문자열을 직접 리터럴로 사용하여 해당 문자열을 검색하기 위해 사용
# import re
# from copy import deepcopy
#
# # 해당 조합의 중복여부 확인하기 위한 리스트
# overlap_check = []
#
# def DFS(idx, candidates, arr, size):
#     global answer, overlap_check
#
#     # 조합 끝까지 전부 확인한 경우
#     if idx == len(candidates):
#         # banned_id 길이와 일치하고, 중복된 조합 아닌 경우
#         if len(arr) == size and arr not in overlap_check:
#             # 조합 리스트에 저장
#             overlap_check.append(deepcopy(arr))
#         return
#
#     # 각 banned_id 패턴별로 가능한 경우의 수를 토대로 조합을 만든다
#     for each_id in candidates[idx]:
#         # 만약 조합에 id가 없을 경우
#         if each_id not in arr:
#             # 조합에 저장
#             arr.add(each_id)
#             DFS(idx+1, candidates, arr, size)
#             # 백트래킹
#             arr.remove(each_id)
#
# def solution(user_id, banned_id):
#     candidates = []
#
#     for i in range(len(banned_id)):
#         # banned id여부를 체크할 정규식을 만든다.
#         banned_id[i] = re.compile("^" + banned_id[i].replace("*", "([0-9]|[a-z])") + "$")
#         temp = set()
#         # 해당 정규식으로 매칭할 수 있는 user_id를 저장한다
#         for each_user in user_id:
#             if banned_id[i].match(each_user):
#                 temp.add(each_user)
#
#         # 각 banned_id 패턴에 부합하는 user id 조합을 저장한다.
#         candidates.append(temp)
#
#     DFS(0, candidates, set(), len(banned_id))
#     return len(overlap_check)