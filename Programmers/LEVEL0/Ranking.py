# Restart 16. 등수 매기기

# My Solution
'''
Use one more list that sort average score
and iterate average list and find index at sorting average score
'''
def solution(score):
    answer = []

    avg_score = [sum(sc) / len(sc) for sc in score]
    avg_score_sort = sorted(avg_score, reverse = True)
    for avg in avg_score:
        answer.append(avg_score_sort.index(avg) + 1)
    return answer

score_1 = [[80, 70], [90, 50], [40, 70], [50, 80]]
score_2 = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]

print(solution(score_1))
print(solution(score_2))