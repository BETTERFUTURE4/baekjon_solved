import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
max = max(arr)
sum = 0

for i in arr:
  sum += i/max*100

print(sum / len(arr))