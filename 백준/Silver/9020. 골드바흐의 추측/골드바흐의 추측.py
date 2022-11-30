import sys

MIN = 4
MAX = 10000

prime = [False,False] + [True] * (MAX-1)

for i in range(2,int(MAX**0.5)+1):
  if prime[i]:
    for k in range(i*2,MAX+1, i):
      prime[k] = False

T = int(input())

for i in range(T):
  n = int(sys.stdin.readline())
  for k in range(n//2,1,-1):
    if prime[k] and prime[n-k]:
      print(k, n-k)
      break