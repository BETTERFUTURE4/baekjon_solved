n = int(input())

for i in range(n):
  x1, y1, r1, x2, y2, r2 = list(map(int,input().split()))
  
  m = ((x2-x1)**2 + (y2-y1)**2)**0.5
  
  if m == 0 and r1 == r2:
    print(-1)
  elif r1 + r2 < m or abs(r2-r1) > m:
    print(0)
  elif r1 + r2 == m or abs(r2-r1) == m:
    print(1)
  else:
    print(2)