# 6. 다리를 지나는 트럭

# 조금만 더 생각해 보지...
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer

bridge_length_1 = 2
bridge_length_2 = 100
bridge_length_3 = 100

weight_1 = 10
weight_2 = 100
weight_3 = 100

truck_weights_1 = [7, 4, 5, 6]
truck_weights_2 = [10]
truck_weights_3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# print(solution(bridge_length_1, weight_1, truck_weights_1))
# print(solution(bridge_length_2, weight_2, truck_weights_2))
# print(solution(bridge_length_3, weight_3, truck_weights_3))


from collections import deque
def solution_mine(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    bridge = deque(0 for _ in range(bridge_length))

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)
        answer += 1

    answer += bridge_length
    return answer

print(solution_mine(bridge_length_1, weight_1, truck_weights_1))
print(solution_mine(bridge_length_2, weight_2, truck_weights_2))
print(solution_mine(bridge_length_3, weight_3, truck_weights_3))

def solution_best(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step