def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = [0] * bridge_length
    sum_bridge = 0

    while truck_weights:
        second += 1
        sum_bridge -= bridge.pop()
        bridge = [0] + bridge
        if sum_bridge + truck_weights[0] <= weight:
            bridge[0] = truck_weights.pop(0)
            sum_bridge += bridge[0]
    return second + bridge_length