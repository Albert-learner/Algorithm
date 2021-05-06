# 19. 모의고사

def solution(answers):
    answer = []

    # 1, 2, 3번 수포자들 규칙 저장 리스트
    people = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    # 3명 수포자들 맞춘 결과 저장 리스트
    results = []

    for person in people:
        results.append(sum([cost == person[idx % len(person)] for idx, cost in enumerate(answers)]))

    answer = [i for i, res in enumerate(results, 1) if max(results) == res]
    return answer

answers_1 = [1, 2, 3, 4, 5]
answers_2 = [1, 3, 2, 4, 2]

print(solution(answers_1))
print(solution(answers_2))

