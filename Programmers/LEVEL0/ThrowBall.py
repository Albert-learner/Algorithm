# Restart 7. 공 던지기

# My Solution
def solution(numbers, k):
    answer = 0

    quote = 0
    if len(numbers) < k * 2:
        quote = (k * 2) // len(numbers)
    else:
        answer = numbers[0::2][k - 1]
        return answer

    numbers *= (1 + quote)
    answer = numbers[0::2][k - 1]
    return answer

numbers_1 = [1, 2, 3]
numbers_2 = [1, 2, 3, 4, 5, 6]
numbers_3 = [1, 2, 3]

k_1 = 2
k_2 = 5
k_3 = 3

print(solution(numbers_1, k_1))
print(solution(numbers_2, k_2))
print(solution(numbers_3, k_3))

# Solution Best by using math
def solution_best(numbers, k):
    answer = 2 * (k - 1) % numbers[-1] + 1

    return answer

print(solution_best(numbers_1, k_1))
print(solution_best(numbers_2, k_2))
print(solution_best(numbers_3, k_3))