from itertools import permutations

def getCount(k, dungeons):
    answer = 0
    for dungeon in dungeons:
        if dungeon[0] <= k:
            k -= dungeon[1]
            answer += 1
        if k <= 0:
            break
    return answer

def solution(k, dungeons):
    arr = list()
    for dungeonsGo in list(permutations(dungeons, len(dungeons))):
        arr.append(getCount(k, dungeonsGo))
    return max(arr)