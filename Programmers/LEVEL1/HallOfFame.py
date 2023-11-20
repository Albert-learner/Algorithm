# Restart 46. 명예의 전당(1)

def solution(k, score):
    answer = []

    k_scores = []
    for sc in score:
        k_scores.append(sc)
        k_scores.sort(reverse = True)

        if len(k_scores) > k:
            k_scores.pop()

        answer.append(min(k_scores))

    return answer

k_1 = 3
k_2 = 4

score_1 = [10, 100, 20, 150, 1, 100, 200]
score_2 = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

print(solution(k_1, score_1))
print(solution(k_2, score_2))