xa = []
ya = []
for i in range(3):
  x, y = map(int,input().split())
  if x in xa:
    xa.remove(x)
  else: xa.append(x)
  
  if y in ya:
    ya.remove(y)
  else: ya.append(y)

print(xa[0],ya[0])