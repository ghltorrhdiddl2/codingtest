def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]  # [0, 0]

    while bridge:
        time += 1
        bridge.pop(0)   # [0]

        if truck_weights:
            if sum(bridge)+truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


#----------더 빠른 방법----------------------
# deque로 popleft()사용!
from collections import deque
def ssolution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])  # deque([0, 0])
    bridge_weight = 0

    while bridge:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1

        if truck_weights:
            if bridge_weight+truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                bridge_weight += t
            else:
                bridge.append(0)

    return time


print(ssolution(2, 10, [7,4,5,6]))
print(ssolution(100, 100, [10]))
print(ssolution(100, 100, [10,10,10,10,10,10,10,10,10,10]))





