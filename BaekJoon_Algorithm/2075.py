# 2075. N번째 큰 수

"""
I didn't solve this problem by myself. I have to think about Memory Excess and Time Excess.
And the key is that using queue data structure for all data is wrong in here.
See this again.
"""
# # 1. My Solution(Wrong, memory excess)
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
#
# graph_sort = sorted(sum(graph, []), reverse=True)
# print(graph_sort[N - 1])

# 1. My Solution
import heapq as hq

N = int(input())
graph = []

for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(graph) < N:
            hq.heappush(graph, number)
        else:
            if graph[0] < number:
                hq.heappop(graph)
                hq.heappush(graph, number)

print(graph[0])


# 2. Not my Solution
import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
=>
35
"""