go = True

while go:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    go = False
  else :
    print(a+b)