# 19. 표 편집

def solution(n, k, cmd):
    answer = ''

    linked_list = {i : [i - 1, i + 1] for i in range(1, n + 1)}
    OX = ['O' for i in range(1, n + 1)]
    stack = []

    k += 1

    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k - 1] = 'X'

            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next
        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now - 1] = 'O'

            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    answer = ''.join(OX)
    return answer

n_1 = 8
n_2 = 8

k_1 = 2
k_2 = 2

cmd_1 = ["D 2",
         "C",
         "U 3",
         "C",
         "D 4",
         "C",
         "U 2",
         "Z",
         "Z"]

cmd_2 = ["D 2",
         "C",
         "U 3",
         "C",
         "D 4",
         "C",
         "U 2",
         "Z",
         "Z",
         "U 1",
         "C"]

# print(solution(n_1, k_1, cmd_1))
# print(solution(n_2, k_2, cmd_2))

import heapq
def solution_best(n, k, cmds):
    answer = ''

    def inverse(num):
        return -num

    max_heap = list(map(inverse, range(k)))
    min_heap = list(range(k, n))
    deleted = ['O' for _ in range(n)]
    deleted_stack = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for cmd in cmds:
        command = cmd.split()
        if len(command) > 1:
            num = command[1]
            command = command[0]
            num = int(num)
            if command == 'D':
                for _ in range(num):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
            else:
                for _ in range(num):
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
        else:
            command = command[0]
            if command == 'C':
                delete_num = heapq.heappop(min_heap)
                deleted_stack.append(delete_num)
                deleted[delete_num] = 'X'
                if len(min_heap) == 0:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
            else:
                restore_num = deleted_stack.pop()
                deleted[restore_num] = 'O'
                if min_heap[0] > restore_num:
                    heapq.heappush(max_heap, -restore_num)
                else:
                    heapq.heappush(min_heap, restore_num)
    answer = ''.join(deleted)
    return answer

# print(solution_best(n_1, k_1, cmd_1))
# print(solution_best(n_2, k_2, cmd_2))