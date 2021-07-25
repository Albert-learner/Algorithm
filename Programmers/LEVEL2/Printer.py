# 55. 프린터

'''
큰 값 순서대로 정렬을 하더라도 우선순위가 같은 것들의 경우가 문제
가장 큰 값 뒤에 나온 것들을 먼저 뽑고 그 다음에 이전에 못 뽑은 것들을
뽑아야 함
'''
def solution(priorities, location):
    answer = 0

    print_lst = [(chr(65 + idx), priority) for idx, priority in enumerate(priorities)]
    waiting_q = []
    max_p = 0

    while print_lst:
        front = print_lst.pop(0)
        priority = front[1]
        rest_lst = [priority for name, priority in print_lst]

        if rest_lst:
            max_p = max(rest_lst)

        if priority >= max_p:
            waiting_q.append(front)
        else:
            print_lst.append(front)

    for print_idx, item in enumerate(waiting_q):
        if item[0] == chr(65 + location):
            answer += 1
            break
        answer += 1
    return answer

priorities_1 = [2, 1, 3, 2]
priorities_2 = [1, 1, 9, 1, 1, 1]

location_1 = 2
location_2 = 0

print(solution(priorities_1, location_1))
print(solution(priorities_2, location_2))

def solution_other(priorities, location):
    pi_list = [(p, i) for i, p in enumerate(priorities)]
    waiting_q = []
    max_p = 0
    answer = 0

    while pi_list:
        pi = pi_list.pop(0)
        priority = pi[0]
        p_list = [priority for priority, idx in pi_list]
        if p_list:
            max_p = max(p_list)

        if priority >= max_p:
            waiting_q.append(pi)
        else:
            pi_list.append(pi)

    for i, item in enumerate(waiting_q):
        if item[1] == location:
            answer = i + 1
            break

    return answer

# print(solution_other(priorities_1, location_1))
# print(solution_other(priorities_2, location_2))

def solution_best(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# print(solution_best(priorities_1, location_1))
# print(solution_best(priorities_2, location_2))
