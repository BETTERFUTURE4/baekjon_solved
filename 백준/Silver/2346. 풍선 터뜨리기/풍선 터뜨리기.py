def moveIdx(dicc, nowIdx):
    nowNum = dicc[nowIdx][0]
    plma = 1
    if nowNum < 0:
        plma = -1
    
    while nowNum != 0:
        nowIdx += plma
        nowIdx %= len(arr)
        if dicc[nowIdx][1] == True:
            nowNum -= plma
    return nowIdx

N = int(input())
arr = list(map(int, input().split()))
dicc = list()
for i in range(len(arr)):
    dicc.append([arr[i], True])

nowIdx = 0
popArr = [1]
dicc[0][1] = False
while len(popArr) != len(arr):
    nowIdx = moveIdx(dicc, nowIdx)
    dicc[nowIdx][1] = False
    popArr.append(nowIdx+1)

print(" ".join([str(e) for e in popArr]))