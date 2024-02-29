# 1635. 1 또는 -1

"""
This code is not passing Baekjoon Server.
I use Overlapping combination to solve this problem, but I got Mermory Error.
The error is still going on.
"""
# 1. My Solution
def generate_combinations(length):
    if length == 0:
        return [[]]
    else:
        previous_combinations = generate_combinations(length - 1)
        new_combinations = []
        for combination in previous_combinations:
            new_combinations.append(combination + [-1])
            new_combinations.append(combination + [1])
        return new_combinations

def find_zero_sum_combinations(sequences):
    zero_sum_combinations = []
    for sequence in sequences:
        combinations = generate_combinations(len(sequence))
        for combination in combinations:
            if sum(a*b for a, b in zip(sequence, combination)) == 0:
                zero_sum_combinations.append(combination)
                break
    return zero_sum_combinations

# 입력을 받습니다.
N, M = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(M)]

# 0인 조합을 찾습니다.
zero_sum_combinations = find_zero_sum_combinations(sequences)

# 결과를 출력합니다.
for combination in zero_sum_combinations:
    print(*combination)

# 2. Not my Solution


"""
4 6
-1 -1 -1 -1
-1 1 -1 -1
1 1 1 1
1 -1 -1 -1
1 -1 1 1
1 1 -1 -1
================
-1 1 -1 1
1 -1 -1 -1
-1 1 -1 1
1 -1 1 1
1 -1 -1 -1
-1 1 -1 1
"""