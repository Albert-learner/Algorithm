# KAKAO Tech 기출 문제 1. 두 큐 합 같게 만들기

from collections import deque
'''
Using Queue but I think in different ways.
My way is to make queue1 and queue2 with one total queue.
And multiply 2 for total queue and compare front queue and rear queue
But I don't know how to implement it. 
So follow queue solution
'''
def solution(queue1, queue2):
    answer = 0

    que1, que2 = deque(queue1), deque(queue2)
    que1_sum, que2_sum = sum(queue1), sum(queue2)
    total_sum = que1_sum + que2_sum

    if total_sum % 2 != 0:
        return -1

    cnt = 0
    while que1_sum != que2_sum:
        if answer > len(que1) + len(que2) + 1:
            return -1

        if que1_sum < que2_sum:
            que2_num = que2.popleft()
            que1.append(que2_num)
            que1_sum += que2_num
            que2_sum -= que2_num
        else:
            que1_num = que1.popleft()
            que2.append(que1_num)
            que2_sum += que1_num
            que1_sum -= que1_num

        answer += 1

    return answer

queue1_1 = [3, 2, 7, 2]
queue1_2 = [1, 2, 1, 2]
queue1_3 = [1, 1]

queue2_1 = [4, 6, 5, 1]
queue2_2 = [1, 10, 1, 2]
queue2_3 = [1, 5]

print(solution(queue1_1, queue2_1))
print(solution(queue1_2, queue2_2))
print(solution(queue1_3, queue2_3))
