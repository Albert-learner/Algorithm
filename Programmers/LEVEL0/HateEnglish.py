# Restart 8. 영어가 싫어요

# My Solution
import re
def solution(numbers):
    answer = 0

    numbers = re.sub(r'zero', '0', numbers)
    numbers = re.sub(r'one', '1', numbers)
    numbers = re.sub(r'two', '2', numbers)
    numbers = re.sub(r'three', '3', numbers)
    numbers = re.sub(r'four', '4', numbers)
    numbers = re.sub(r'five', '5', numbers)
    numbers = re.sub(r'six', '6', numbers)
    numbers = re.sub(r'seven', '7', numbers)
    numbers = re.sub(r'eight', '8', numbers)
    numbers = re.sub(r'nine', '9', numbers)

    answer = int(numbers)
    return answer

numbers_1 = "onetwothreefourfivesixseveneightnine"
numbers_2 = "onefourzerosixseven"

print(solution(numbers_1))
print(solution(numbers_2))

def solution_other(numbers):
    answer = 0

    for num, eng in enumerate(['zero', 'one', 'two',
                               'three', 'four', 'five',
                                'six', 'seven', 'eight',
                                'nine']):
        numbers = numbers.replace(eng, str(num))

    answer = int(numbers)
    return answer

print(solution_other(numbers_1))
print(solution_other(numbers_2))