n = int(input())

for i in range(n):
  generator = i
  for j in str(i):
    generator += int(j)
  if generator == n:
    print(i)
    break
else:
  print(0)