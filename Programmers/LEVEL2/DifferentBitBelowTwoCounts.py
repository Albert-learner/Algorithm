# 43. 2개 이하로 다른 비트

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        answer.append(int(''.join(bin_number), 2))
    return answer

numbers_1 = [2, 7]

print(solution(numbers_1))

'''
numbers 리스트 안에 값을 기준으로 이진수로 바꿨을 때 한 자리를 더 추가한 값들 중 가장 큰 값
ex) 2 -> 010(2) -> 111(2) -> 7값을 기준으로
3 ~ 7까지의 수를 이진수로 바꿔서 비교
ex) 3 -> 011(2) -> 010(2)와 011(2) 각 자리별로 비교
비트가 다른 것들의 개수를 bit_checks변수에 저장
bit_checks가 2보다 작은 수들 중에 값이 제일 작은 수 반환(여기가 안 됨)
그리고 만약에 이게 해결이 되더라도 시간 초과로 걸릴 듯...
'''
def solution_mine(numbers):
    answer = 0

    bin_number_lst = []
    for number in numbers:
        bin_number = bin(number)[2:]
        max_num = int((len(bin_number) + 1) * '1', 2)
        bit_checks = 0
        for num in range(number + 1, max_num + 1):
            b_num = bin(num)[2:]
            for bit1, bit2 in zip(bin_number, b_num):
                if bit_checks <= 2:
                    if bit1 != bit2:
                        bit_checks += 1
                else:
                    break

            if bit_checks <= 2:
                bin_number_lst.append(num)

            bit_checks = 0

    print(bin_number_lst)
    return answer

def solution_best(numbers):
    answer = []

    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val + 1)) >> 2) + val + 1)
    return answer

print(solution_best(numbers_1))
