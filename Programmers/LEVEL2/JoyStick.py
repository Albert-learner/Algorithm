# 9. 조이스틱

# 문제 이해가 어려웠어...
def solution(name):
    idx, answer = 0, 0
    min_move = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
                for i in name]

    while True:
        answer += min_move[idx]
        min_move[idx] = 0
        if sum(min_move) == 0:
            break
        left, right = 1, 1
        while min_move[idx - left] == 0:
            left += 1
        while min_move[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right

    return answer

name_1 = 'JEROEN'
name_2 = 'JAN'

print(solution(name_1))
print(solution(name_2))