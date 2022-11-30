import math

T = int(input())
for i in range(T):
  x,y = list(map(int,input().split()))
  n = math.ceil((y - x)**0.5)
  
  if (n-1) * n < y - x <= n*n:
    print(2*n-1)
  elif (n-1)*(n-1) < y - x <= (n-1) * n:
    print(2*n-2)