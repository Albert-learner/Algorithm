# 1747. 소수 & 팰린드롬

"""
I almost solve this problem by myself.
I catch Palindrome and Prime number implementation by my reference code, so see it again for perfect implementation.
But I miss except conditions that if the number is 1 and number is 1000000.
"""
# 1. My Solution
N = int(input())

def is_prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True

    return False

answer = 0
for num in range(N, 1000001):
    if num == 1:
        continue
    if is_prime_number(num) and is_palindrome(num):
        answer = num
        break

if answer == 0:
    answer = 1003001

print(answer)

# 2. Not my Solution
import math

def isPrime(x): # 소수인지 판별해주는 함수
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

N = int(input())
result = 0

for i in range(N, 1000001): # 입력값 N 부터 최대값 까지 순환
    if i == 1: # 1은 소수가 아니기 때문에 예외처리
        continue
    if str(i) == str(i)[::-1]: # 팰림드롬 수 일 경우
        if isPrime(i) == True: # 소수 판별 함수 적용
            result = i
            break

if result == 0: # 입력값이 만약 최대 값 100만일 경우
    result = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용

print(result)


"""
31
=>
101
================
1000000
=>
1003001
"""