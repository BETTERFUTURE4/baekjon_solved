from itertools import combinations

def getArrSum(L, orderArr):
    steminas = [L[e] for e in orderArr]
    return sum(steminas)

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dic = [i for i in range(N)]

finalDic = []

for i in range(1, N+1):
    finalDic.extend(combinations(dic, i))

joys = []

for d in finalDic:
    if getArrSum(L,d) < 100:
        joys.append(getArrSum(J,d))

if not joys:
    print(0)
else:
    print(max(joys))
