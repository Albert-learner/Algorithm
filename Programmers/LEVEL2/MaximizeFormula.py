# 39. 수식 최대화

'''
Not solve this problem by myself. I think 80% I did, but I don`t know
how to calculate formula.
'''
import re
from itertools import permutations
def solution(expression):
    answer = 0
    operators = [x for x in ['-', '+', '*'] if x in expression]
    operators_perm = list(permutations(operators))

    expression = re.split('([^0-9])', expression)
    for order in operators_perm:
        expression_cpy = expression[:]
        for operator in order:
            # 이 부분 주목
            while operator in expression_cpy:
                operator_idx = expression_cpy.index(operator)
                formula_cost = str(eval(expression_cpy[operator_idx - 1] +
                                        expression_cpy[operator_idx] +
                                        expression_cpy[operator_idx + 1]))
                expression_cpy[operator_idx - 1] = formula_cost
                expression_cpy = expression_cpy[:operator_idx] + expression_cpy[operator_idx + 2:]
        answer = max(answer, abs((int(expression_cpy[-1]))))
    return answer

expression_1 = '100-200*300-500+20'
expression_2 = '50*6-3*2'

# print(solution(expression_1))
# print(solution(expression_2))

'''
100-200*300-500+20 이 예의 경우
['100', '-', '200], ['200', '*', '300'], ... , ['500', '+', '20']
형태로 만드는 것은 성공하였고, 각 연산자 별로 우선순위를 조합으로 만드는 것까지 
성공하였으나, 
계산을 수행할 때 바뀌는 과정을 어떻게 구현해야할지 감이 안 잡힘.
'''
import re
from itertools import permutations
def solution_mine(expression):
    answer = 0

    # [('100', '-'), '200], [('200', '*'), '300], ...
    p = re.compile('(\d+)([-+*]?)')
    expression = p.findall(expression)
    formula_lst = []
    for (express1_num, operator), express2 in zip(expression, expression[1:]):
        formula_lst.append([express1_num, operator, express2[0]])
    print(formula_lst)

    # 연산자 우선순위 순열
    operators = set([i[1] for i in formula_lst if i[1] in ['-', '+', '*']])
    operators_perm = list(permutations(operators, len(operators)))
    print(operators_perm)

    answer_lst = []
    for order in operators_perm:
        formula_cost = 0
        for operator in order:
            for formula in formula_lst:
                if operator in formula:
                    formula_cost += eval(''.join(formula))
                    del formula_lst[formula_lst.index(formula)]
        answer_lst.append(formula_cost)

    print(answer_lst)
    return answer

# 다른 풀이(재귀)
def calculate(priority, n, expression):
    if n == 2:
        return str(eval(expression))

    if priority[n] == '*':
        result = eval('*'.join([calculate(priority, n + 1, e)
                                for e in expression.split('*')]))
    if priority[n] == '+':
        result = eval('+'.join([calculate(priority, n + 1, e)
                                for e in expression.split('+')]))
    if priority[n] == '-':
        result = eval('-'.join([calculate(priority, n + 1, e)
                                for e in expression.split('-')]))
    return str(result)

def solution_other(expression):
    answer = 0

    priorities = (list(permutations(['+', '-', '*'], 3)))
    for priority in priorities:
        result = int(calculate(priority, 0, expression))
        answer = max(answer, abs(result))

    return answer

# print(solution_other(expression_1))
# print(solution_other(expression_2))

# 제일 좋다고 생각되는 풀이(재귀랑 거의 비슷한 구조)
def solution_best(expression):
    answer = []

    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    for operator in operations:
        first = operator[0]
        second = operator[1]
        temp_list = []
        for e in expression.split(first):
            temp = [f'({i})' for i in e.split(second)]
            temp_list.append(f'{second.join(temp)}')
        answer.append(abs(eval(first.join(temp_list))))
    return max(answer)

print(solution_best(expression_1))
print(solution_best(expression_2))

