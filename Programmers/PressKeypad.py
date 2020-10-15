# 24. 키패드 누르기

# 내가 못 품 ... 2, 5, 8, 0일때 생각
def solution(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            lastL = number
        elif number in [3, 6, 9]:
            answer += 'R'
            lastR = number
        else:
            number = 11 if number == 0 else number

            absL = abs(number - lastL)
            absR = abs(number - lastR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                lastR = number
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                lastL = number
            else:
                if hand == 'left':
                    answer += 'L'
                    lastL = number
                else:
                    answer += 'R'
                    lastR = number

    return answer

numbers_1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers_2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

hand_1 = 'right'
hand_2 = 'left'
hand_3 = 'right'

print(solution(numbers_1, hand_1))
print(solution(numbers_2, hand_2))
print(solution(numbers_3, hand_3))
