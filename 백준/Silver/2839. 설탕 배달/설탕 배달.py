n = int(input())

for five in range(int(n/5),-1,-1):
  three = (n - 5*five) / 3
  if three == int(three) :
    print(int(five + three))
    case = True
    break
else:
  print(-1)