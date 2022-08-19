from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    moves = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    while len(truck_weights) or bridge_weight > 0:
        answer += 1
        out_truck = moves.popleft()
        bridge_weight -= out_truck
        
        if len(truck_weights) and bridge_weight + truck_weights[0] <= weight:
            int_truck = truck_weights.popleft()
            moves.append(int_truck)
            bridge_weight += int_truck
        else:
            moves.append(0)

    return answer