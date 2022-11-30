import sys
import math

MAX = 123456
arr = [0,0] + [1] * (2*MAX-1)
for i in range(2,int(math.sqrt(2*MAX))+1):
  if arr[i]:
    for k in range(2*i,2*MAX+1,i):
      arr[k] = 0
while True:
  n = int(sys.stdin.readline())
  if n == 0: break
  
  print(sum(arr[n+1:2*n+1]))