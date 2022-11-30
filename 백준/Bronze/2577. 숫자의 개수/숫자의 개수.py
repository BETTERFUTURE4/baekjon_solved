a = int(input())
b = int(input())
c = int(input())
arr = list(str(a*b*c))

count = [0,0,0,0,0,0,0,0,0,0]
for i in arr:
  count[int(i)] += 1

for i in count:
  print(i)