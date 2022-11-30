while True:
  a,b,c = list(map(int,input().split()))
  if a==0 and b==0 and c==0:
    break
  
  arr = sorted([a,b,c])

  if arr[0]**2 + arr[1]**2 == arr[2]**2:
    print("right")
  else:
    print("wrong")