# Restart 42. 둘만의 암호

'''
This problem also requires the reversal of thoughts.
I didn't solve this problem by myself.
My Solution is wrong at test case 2.
'''
def solution(s, skip, index):
    answer = ""

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alps = sorted(set(alphabets) - set(skip))
    alp_cnts = len(alps)

    for sub_s in s:
        answer += alps[(alps.index(sub_s) + index) % alp_cnts]
    return answer

'''
This Solution can't solve test case 2.
'''
def solution_mine(s, skip, index):
    answer = ''

    alphabets_lst = [chr(97 + alp_idx) for alp_idx in range(26)]
    changed_str = ''
    for sub_s in s:
        sub_s_idx_lst = [chr(ord(sub_s) + idx) for idx in range(1, index + 1)]
        remove_sub_s_idx_lst = sorted(list(set(sub_s_idx_lst).difference(skip)))
        if len(remove_sub_s_idx_lst) != index:
            diff_cnts = int(abs(index - len(remove_sub_s_idx_lst)))
            last_remove_sub_s = remove_sub_s_idx_lst[-1]
            for diff_cnt in range(1, diff_cnts + 1):
                remove_sub_s_idx_lst.append(chr(ord(last_remove_sub_s) + diff_cnt))
            changed_str += remove_sub_s_idx_lst[-1]
        else:
            changed_str += remove_sub_s_idx_lst[-1]

    for chgd_idx in range(len(changed_str)):
        if changed_str[chgd_idx] not in alphabets_lst:
            return_cnts = ord(changed_str[chgd_idx]) - ord('z') - 1
            answer += alphabets_lst[return_cnts]
        else:
            answer += changed_str[chgd_idx]

    return answer

'''
Same as solution, but it's a little bit simple.
'''
def solution_other(s, skip, index):
    answer = ''

    alps = [chr(alp) for alp in range(ord('a'), ord('z') + 1)
            if chr(alp) not in skip]
    answer = ''.join([alps[(alps.index(sub_s) + index) % len(alps)]
                      for sub_s in s])
    return answer

'''
Similar with solution, but it's the best.
'''
from string import ascii_lowercase
def solution_best(s, skip, index):
    answer = ''

    alps = set(ascii_lowercase)
    alps -= set(skip)
    alps = sorted(alps)
    alps_len = len(alps)

    alps_dict = {alpha : idx for idx, alpha in enumerate(alps)}

    for sub_s in s:
        answer += alps[(alps_dict[sub_s] + index) % alps_len]
    return answer

s_1 = "aukks"
s_2 = "zzzz"

skip_1 = "wbqd"
skip_2 = "abcd"

index_1 = 5
index_2 = 1

print(solution(s_1, skip_1, index_1))
print(solution(s_2, skip_2, index_2))

print(solution_other(s_1, skip_1, index_1))
print(solution_other(s_2, skip_2, index_2))

print(solution_best(s_1, skip_1, index_1))
print(solution_best(s_2, skip_2, index_2))