# 11. H-Index

# 정렬 후 (인덱스 + 1)값과 리스트 값 비교
def solution(citations):
    answer = 0

    h_lst = sorted(citations, reverse = True)
    h_index_lst = [min(i + 1, h_lst[i]) for i in range(len(h_lst))]

    answer = max(h_index_lst)
    return answer

citations_1 = [3, 0, 6, 1, 5]
citations_2 = [6, 6, 6, 6, 6]

print(solution(citations_1))
print(solution(citations_2))

def solution_other(citations):
    answer = len(citations)
    citations.sort()

    while True:
        cnt = 0
        for val in citations:
            if val >= answer:
                cnt += 1
            if answer <= cnt:
                return answer
        answer -= 1

    return answer

# print(solution_other(citations_1))
# print(solution_other(citations_2))

def solution_best(citations):

    answer = max([min(i+1, sorted(citations, reverse=True)[i]) for i in range(len(citations))])

    return answer

# print(solution_best(citations_1))
# print(solution_best(citations_2))