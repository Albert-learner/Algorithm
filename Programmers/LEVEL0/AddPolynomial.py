# Restart 19. 다항식 더하기
def solution(polynomial):
    answer = ''

    x_coef, const = 0, 0
    polynomial = polynomial.split(' + ')
    for poly in polynomial:
        if 'x' in poly:
            if poly[:-1]:
                x_coef += int(poly[:-1])
            else:
                x_coef += 1
        else:
            const += int(poly)

    if x_coef and const:
        answer = f'{x_coef}x + {const}' if x_coef > 1 else f'x + {const}'
    elif x_coef and not const:
        answer = f'{x_coef}x' if x_coef > 1 else f'x'
    else:
        answer = f'{const}'
    return answer

polynomial_1 = "3x + 7 + x"
polynomial_2 = "x + x + x"

print(solution(polynomial_1))
print(solution(polynomial_2))

def solution_other(polynomial):
    answer = ''
    x_coef, num = 0, 0
    polynomial = polynomial.split(' + ')
    for poly in polynomial:
        if 'x' in poly:
            if len(poly) == 1:
                x_coef += 1
            else:
                x_coef += int(poly[:-1])
        else:
            num += int(poly)

    if x_coef == 0 and num == 0:
        return '0'
    if x_coef == 0:
        return str(num)
    if x_coef == 1:
        x_coef = ''
    if num == 0:
        return str(x_coef) + 'x'

    answer = str(x_coef) + 'x + ' + str(num)
    return answer

# print(solution_other(polynomial_1))
# print(solution_other(polynomial_2))