# 53. 신고 결과 받기

from collections import Counter
def solution(id_list, report, k):
    answer = []

    check_list = []
    report_dict = {id : [] for id in id_list}
    for rep in report:
        reporter, reported = rep.split()
        if reported not in report_dict[reporter]:
            report_dict[reporter].append(reported)
            check_list.append(reported)

    cnt_dict = Counter(check_list)
    for id in id_list:
        answer.append(len([check for check in report_dict[id]
                           if cnt_dict[check] >= k]))
    return answer

id_list_1 = ["muzi", "frodo", "apeach", "neo"]
id_list_2 = ["con", "ryan"]

report_1 = ["muzi frodo", "apeach frodo", "frodo neo",
            "muzi neo", "apeach muzi"]
report_2 = ["ryan con", "ryan con",
            "ryan con", "ryan con"]

k_1 = 2
k_2 = 3

print(solution(id_list_1, report_1, k_1))
print(solution(id_list_2, report_2, k_2))

def solution_best(id_list, report, k):
    answer = [0] * len(id_list)

    reports = {id : 0 for id in id_list}
    for rep in set(report):
        reports[rep.split()[1]] += 1

    for rep in set(report):
        if reports[rep.split()[1]] >= k:
            answer[id_list.index(rep.split()[0])] += 1
    return answer

print(solution_best(id_list_1, report_1, k_1))
print(solution_best(id_list_2, report_2, k_2))