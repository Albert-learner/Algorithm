# Restart 2. A로 B 만들기

# My Solution
from collections import Counter
def solution(before, after):
    bef_counter = Counter(before)
    aft_counter = Counter(after)

    answer = 1 if bef_counter.items() == aft_counter.items() else 0
    return answer

before_1 = "olleh"
before_2 = "allpe"

after_1 = "hello"
after_2 = "apple"

print(solution(before_1, after_1))
print(solution(before_2, after_2))

# Best Solution that I thought
def solution_best(before, after):
    answer = 1 if sorted(before) == sorted(after) else 0

    return answer

print(solution_best(before_1, after_1))
print(solution_best(before_2, after_2))