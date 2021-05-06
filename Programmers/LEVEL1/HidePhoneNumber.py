# 35. 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''

    for i in range(len(phone_number)):
        if i < len(phone_number) - 4:
            answer += '*'
        else:
            answer += phone_number[i]
    return answer

phone_number1 = '01033334444'
phone_number2 = '027778888'

print(solution(phone_number1))
print(solution(phone_number2))

def solution_best(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]

    return answer

print(solution_best(phone_number1))
print(solution_best(phone_number2))