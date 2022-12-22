def solution(논문들):
    # if len(논문들) == 1 and 논문들[0] == 0:
    #     return 0
    # elif len(논문들) == 1 and 논문들[0] >= 1:
    #     return 1
    arr = [0] * 10001
    for 논문인용수 in 논문들:
        arr[논문인용수] += 1
    
    for n in range(1,len(arr)):
        if n > sum(arr[n:]):
            return n-1