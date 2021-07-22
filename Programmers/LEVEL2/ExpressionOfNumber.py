# 54. 숫자의 표현

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break

    return answer

n_1 = 15

print(solution(n_1))

# 등차수열의 합 공식
def solution_best(n):
    # n % i is 0으로 나와있는데 is문법은 보통 같은 객체를 가리킬 때 사용
    answer = len([i for i in range(1, n + 1, 2) if n % i == 0])

    return answer

print(solution_best(n_1))
