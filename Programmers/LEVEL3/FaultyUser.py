# 21. 불량 사용자

from itertools import permutations
def compare(users, banned_id):
    for ban_idx in range(len(banned_id)):
        if len(users[ban_idx]) != len(banned_id[ban_idx]):
            return False

        for usr_idx in range(len(users[ban_idx])):
            if banned_id[ban_idx][usr_idx] == '*':
                continue
            if banned_id[ban_idx][usr_idx] != users[ban_idx][usr_idx]:
                return False

    return True

def solution(user_id, banned_id):
    answer = 0
    user_permutation = list(permutations(user_id, len(banned_id)))
    banned_set = []

    for users in user_permutation:
        if not compare(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in banned_set:
                banned_set.append(users)

    answer = len(banned_set)
    return answer

user_id_1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id_2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id_3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id_1 = ["fr*d*", "abc1**"]
banned_id_2 = ["*rodo", "*rodo", "******"]
banned_id_3 = ["fr*d*", "*rodo", "******", "******"]

# print(solution(user_id_1, banned_id_1))
# print(solution(user_id_2, banned_id_2))
# print(solution(user_id_3, banned_id_3))

from itertools import permutations
def check(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            if j == '*':
                continue
            if i != j:
                return False
        return True

def solution_other(user_id, banned_id):
    answer = 0

    banned_set = []
    for user in permutations(user_id, len(banned_id)):
        count = 0
        for a, b in zip(user, banned_id):
            if check(a, b):
                count += 1

        if count == len(banned_id):
            if set(user) not in banned_set:
                banned_set.append(set(user))

    answer = len(banned_set)
    return answer

# print(solution_other(user_id_1, banned_id_1))
# print(solution_other(user_id_2, banned_id_2))
# print(solution_other(user_id_3, banned_id_3))

import re
import itertools
def solution_best(user_id, banned_id):
    answer = 0

    banned_id = ["'" + ban.replace('*', '\w') + "'"
                 for ban in banned_id]
    possible_list = [re.findall(ban, str(user_id)) for ban in banned_id]
    possible_list = list(itertools.product(*possible_list))

    possible_list = [frozenset(p) for p in possible_list
                     if len(set(p)) == len(banned_id)]
    possible_list = set(possible_list)

    answer = len(possible_list)
    return answer

print(solution_best(user_id_1, banned_id_1))
print(solution_best(user_id_2, banned_id_2))
print(solution_best(user_id_3, banned_id_3))