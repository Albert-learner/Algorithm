# 기사단원의 무기

"""
I almost solve this problem by myself. The key of this problem is finding counts of divisors.
Here's the code of Searching Divisors in Efficient ways.
See it again.
"""
def solution(number, limit, power):
    answer = 0

    numbers = [num for num in range(1, number + 1)]
    divisors_cnt = []
    for num in numbers:
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i < num // i:
                    divisors.append(num // i)
            divisors.sort()

        divisors_cnt.append(len(divisors))

    for divisor_cnt in divisors_cnt:
        if divisor_cnt <= limit:
            answer += divisor_cnt
        else:
            answer += power

    return answer

def solution_other(number, limit, power):
    answer = 0

    numbers = [num for num in range(1, number + 1)]
    divisors_cnt = []
    for num in numbers:
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i < num // i:
                    divisors.append(num // i)
            divisors.sort()

        divisors_cnt.append(len(set(divisors)))

    for divisor_cnt in divisors_cnt:
        if divisor_cnt <= limit:
            answer += divisor_cnt
        else:
            answer += power

    return answer

number_1 = 5
number_2 = 10

limit_1 = 3
limit_2 = 3

power_1 = 2
power_2 = 2

print(solution(number_1, limit_1, power_1))
print(solution(number_2, limit_2, power_2))