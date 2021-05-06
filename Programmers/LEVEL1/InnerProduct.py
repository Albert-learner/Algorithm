# 39. 내적

def solution(a, b):
    answer = 1234567890

    Inner_Product = 0
    for i, j in zip(a, b):
        Inner_Product += i * j

    answer = Inner_Product
    return answer

a_1 = [1, 2, 3, 4]
a_2 = [-1, 0, 1]

b_1 = [-3, -1, 0, 2]
b_2 = [1, 0, -1]

print(solution(a_1, b_1))
print(solution(a_2, b_2))