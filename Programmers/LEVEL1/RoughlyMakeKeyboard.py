# Restart 40. 대충 만든 자판

# Solve this problem by myself. I catched that using dictionary for solving this problem.
# I solve this by finding minimum target character counts to dictionary
def solution(keymap, targets):
    answer = [0] * len(targets)

    minimum_keymap_dict = {}
    keymap_target_idx_lst = sorted([(keym_chr, keym_idx) for keym in keymap for keym_idx, keym_chr in enumerate(keym, 1)],
                                   key = lambda x : x[0])

    for keym_chr, keym_idx in keymap_target_idx_lst:
        if keym_chr not in minimum_keymap_dict:
            minimum_keymap_dict[keym_chr] = keym_idx
        else:
            min_key_value = minimum_keymap_dict[keym_chr]
            if keym_idx < min_key_value:
                minimum_keymap_dict[keym_chr] = keym_idx

    for target_idx in range(len(targets)):
        target = targets[target_idx]
        for target_chr in target:
            if target_chr in minimum_keymap_dict:
                answer[target_idx] += minimum_keymap_dict[target_chr]
            else:
                answer[target_idx] = -1
                break

    return answer

keymap_1 = ["ABACD", "BCEFD"]
keymap_2 = ["AA"]
keymap_3 = ["AGZ", "BSSS"]

targets_1 = ["ABCD","AABB"]
targets_2 = ["B"]
targets_3 = ["ASA","BGZ"]

# Same as other's solution. So I didn't rewind it.
def solution_other(keymap, targets):
    answer = []


    return answer

print(solution(keymap_1, targets_1))
print(solution(keymap_2, targets_2))
print(solution(keymap_3, targets_3))

print(solution_other(keymap_1, targets_1))
print(solution_other(keymap_2, targets_2))
print(solution_other(keymap_3, targets_3))