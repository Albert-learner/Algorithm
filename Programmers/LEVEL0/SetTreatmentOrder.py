# Restart 6. 진료 순서 정하기

# My Solution
def solution(emergency):
    answer = []

    rank_dict = {emer: idx + 1 for idx, emer in enumerate(sorted(emergency, reverse=True))}
    answer = [rank_dict[emer] for emer in emergency]
    return answer

emergency_1 = [3, 76, 24]
emergency_2 = [1, 2, 3, 4, 5, 6, 7]
emergency_3 = [30, 10, 23, 6, 100]

print(solution(emergency_1))
print(solution(emergency_2))
print(solution(emergency_3))

def solution_best(emergency):
    answer = [sorted(emergency, reverse = True).index(emer) + 1 for emer in emergency]

    return answer

print(solution_best(emergency_1))
print(solution_best(emergency_2))
print(solution_best(emergency_3))