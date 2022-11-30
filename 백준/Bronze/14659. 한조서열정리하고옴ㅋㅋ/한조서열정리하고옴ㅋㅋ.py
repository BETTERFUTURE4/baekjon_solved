import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

maxCount = 0
count = 0
maxQQ = arr.pop(0)
if not arr:
    print(0)
else:
    for i,t in enumerate(arr):
        if maxQQ > t:
            count += 1
        else:
            maxCount = max(maxCount, count)
            maxQQ = t
            count = 0
        if i==len(arr)-1:
            maxCount = max(maxCount, count)
            break
        # print(t,"maxQQ:", maxQQ,count,"/max : ",maxCount) 
    print(maxCount)
