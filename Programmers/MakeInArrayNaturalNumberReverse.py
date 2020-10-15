# 30. 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()

    return answer

n_1 = 12345

print(solution(n_1))

def solution_best(n):
    answer = list(map(int, reversed(str(n))))

    return answer

print(solution_best(n_1))