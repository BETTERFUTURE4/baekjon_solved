import sys
import math

def 블럭개수계산(arr,n):
    plusCount = sum([a*(i-n) for i, a in enumerate(arr) if i > n])
    minusCount = sum([a*(n-i) for i, a in enumerate(arr) if i < n])
    return (minusCount, plusCount)

N,M,B = map(int, input().split())
arr = list()
for _ in range(N):
    arr.extend(list(map(int,sys.stdin.readline().split())))

땅높이 = 0
시간 = 6.4 * (10**7) * 2 + 1

numArr = [arr.count(n) for n in range(max(arr)+1)]

for n in range(min(arr), int((math.ceil(sum(arr)+B)/(N*M)))+1):
    부족, 잉여 = 블럭개수계산(numArr, n)
    현재시간 = 잉여*2+부족
    if 시간 < 현재시간:
        break
    땅높이 = n
    시간 = 현재시간

print(시간, 땅높이)
