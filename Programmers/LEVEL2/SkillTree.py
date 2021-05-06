# 7. 스킬트리


def solution(skill, skill_trees):
    answer = 0

    for orders in skill_trees:
        skill_lst = []
        check = True

        for sk in range(len(orders)):
            if orders[sk] in skill:
                skill_lst.append(orders[sk])

        for sk in range(len(skill_lst)):
            if skill_lst[sk] != skill[sk]:
                check = False
                break

        if check == True:
            answer += 1

    return answer

skill_1 = 'CBD'
skill_trees_1 = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill_1, skill_trees_1))