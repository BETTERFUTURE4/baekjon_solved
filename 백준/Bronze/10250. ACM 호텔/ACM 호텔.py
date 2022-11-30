num = int(input())

for i in range(num):
  h, w, n= map(int,input().split())
  one = str((n+h - 1)%h + 1)
  two = str((n+h - 1)//h).zfill(2)
  
  print(one + two)