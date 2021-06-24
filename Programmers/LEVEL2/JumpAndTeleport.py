# 46. 점프와 순간이동

'''
가장 가까운 거리에 있으면서 n값보다 작은 2의 거듭제곱 수만큼 빼고
2500 -> 2500 - 2048
2로 안 나눠질 경우 1씩 더하는 방식
------------------------------------------------------------
입력받은 n값이 0이 될 때까지 n을 2로 나눈 몫과 나머지 구하고
나머지 1일 경우만 count
'''
def solution(n):
    answer = 0

    while n > 0:
        quote, rest = divmod(n, 2)
        n = quote
        if rest != 0:
            answer += 1

    return answer

n_1 = 5
n_2 = 6
n_3 = 5000

print(solution(n_1))
print(solution(n_2))
print(solution(n_3))

def solution_best(n):
    return bin(n).count('1')

print(solution_best(n_1))
print(solution_best(n_2))
print(solution_best(n_3))