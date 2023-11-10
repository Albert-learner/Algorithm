# Restart 39. 덧칠하기

# Solve by relationship between m and section list
def solution(n, m, section):
    answer = 1
    start_colored = section[0]

    for colored in range(1, len(section)):
        if section[colored] - start_colored >= m:
            answer += 1
            start_colored = section[colored]

    return answer

# Solve by using deque
from collections import deque
def solution_other(n, m, section):
    answer = 0
    section = deque(section)

    while section:
        start_colored = section.popleft()
        while section:
            if section[0] >= start_colored + m:
                break
            section.popleft()
        answer += 1
    return answer

n_1 = 8
n_2 = 5
n_3 = 4

m_1 = 4
m_2 = 4
m_3 = 1

section_1 = [2, 3, 6]
section_2 = [1, 3]
section_3 = [1, 2, 3, 4]

print(solution(n_1, m_1, section_1))
print(solution(n_2, m_2, section_2))
print(solution(n_3, m_3, section_3))
print()
print(solution_other(n_1, m_1, section_1))
print(solution_other(n_2, m_2, section_2))
print(solution_other(n_3, m_3, section_3))


# Find how to remove list element that overlapped specific contents
def solution_mine(n, m, section):
    answer = 0

    # Complete Search
    # If colored, cost is 1 else 0(need to be colored)
    wall_sections = [(wall_section, 0) if wall_section in section else (wall_section, 1)
                     for wall_section in list(range(1, n + 1))]

    # Possible cases of colored areas by considering m
    # 8, 4 -> 5 / 5, 4 -> 2 / 4, 1 -> 4
    color_possibles = [wall_sections[start_wall:start_wall + m] for start_wall in range(len(wall_sections) - m + 1)]

    # How to remove cases that are overlapped at specific elements
    # [(1, 1), (2, 0), (3, 0), (4, 1)], [(2, 0), (3, 0), (4, 1), (5, 1)]

    return answer


