n = int(input())

for i in range(n):
  arr = list(map(int, input().split()))
  average = sum(arr[1:])/arr[0]
  num = 0
  for i in range(1, arr[0]+1):
    if arr[i] > average:
      num += 1
  print("%0.3f%%" % (num/arr[0] * 100))