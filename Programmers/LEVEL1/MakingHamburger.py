# 햄버거 만들기

"""
I didn't solve this problem by myself. The key of this problem is Stack.
But I didn't catch how to solve this with stack Data Structure.
See it again.
"""
def solution(ingredient):
    answer = 0

    hamburgers = []
    for material in ingredient:
        hamburgers.append(material)
        if hamburgers[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                hamburgers.pop()

    return answer

ingredient_1 = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient_2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]

print(solution(ingredient_1))
print(solution(ingredient_2))