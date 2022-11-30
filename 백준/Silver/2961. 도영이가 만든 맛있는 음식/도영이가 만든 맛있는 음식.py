from itertools import *

def 차이(arr):
    sin = 1
    ssun = 0
    for a in arr:
        sin *= a[0]
        ssun += a[1]
    return(abs(sin-ssun))

def 튜플들을_리스트들로(arr) :
    result = list()
    for a in arr:
        result.append(list(a))
    return result

재료개수 = int(input())
arr = [list(map(int, input().split())) for i in range(재료개수)]

# arr.sort(key=lambda x:x[0])

comb = list()

for i in range(1,재료개수+1):
    조합 = 튜플들을_리스트들로(combinations(arr,i))
    for zo in 조합:
        comb.append(차이(zo))

print(min(comb))