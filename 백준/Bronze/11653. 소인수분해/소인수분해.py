T = int(input())

i = 2
while T != 1:
  if i <= T**0.5:
    if T % i == 0:
      T = T//i
      print(i)
      i = 2
    else:
      i += 1
  else:
    print(T)
    break