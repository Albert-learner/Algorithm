# Restart 8. 숨어있는 숫자의 덧셈(2)

# My Solution
import re
def solution(my_string):
    answer = 0

    extract_num = re.findall(r'\d+', my_string)
    extract_num_process = [extract_n for extract_n in extract_num if len(extract_n) == len(str(int(extract_n)))]
    answer = sum(list(map(int, extract_num_process)))
    return answer

my_string_1 = "aAb1B2cC34oOp"
my_string_2 = "1a2b3c4d123Z"

print(solution(my_string_1))
print(solution(my_string_2))

import re
def solution_other(my_string):
    answer = sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

    return answer

print(solution_other(my_string_1))
print(solution_other(my_string_2))

# No using re module
def solution_best(my_string):
    extract_num_str = ''.join(i if i.isdigit() else ' ' for i in my_string)
    answer = sum(int(i) for i in extract_num_str.split())

    return answer

print(solution_best(my_string_1))
print(solution_best(my_string_2))