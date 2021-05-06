# 2. 주식가격

# 문제 이해가 잘 안 되가지고... 내 풀이 X
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

prices_1 = [1, 2, 3, 2, 3]

# print(solution(prices_1))

def solution_stack(prices):
    answer = [0] * len(prices)

    stack = []
    for i in range(len(prices)):
        while len(stack) != 0 and prices[i] < prices[stack[len(stack) - 1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)

    while len(stack):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1
    return answer

# print(solution_stack(prices_1))


# 이해가 안 되면 이 풀이가 좀 더 직관적
from collections import deque

def solution_best(prices):
    answer = []

    que_prices = deque(prices)

    while que_prices:
        price = que_prices.popleft()
        # 가격 떨어지지 않는 기간
        up_time = 0
        for n in que_prices:
            up_time += 1
            if price > n:
                break
        answer.append(up_time)
    return answer

print(solution_best(prices_1))
